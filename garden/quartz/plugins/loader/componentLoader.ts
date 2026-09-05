import { componentRegistry } from "../../components/registry"
import { ComponentManifest, PluginManifest } from "./types"
import { QuartzComponentConstructor } from "../../components/types"
import { getPluginSubpathEntry, toFileUrl } from "./gitLoader"

export async function loadComponentsFromPackage(
  pluginName: string,
  manifest: PluginManifest | null,
): Promise<void> {
  if (!manifest?.components) return

  try {
    const componentsPath = getPluginSubpathEntry(pluginName, "./components")

    let componentsModule: Record<string, unknown>
    if (componentsPath) {
      componentsModule = await import(toFileUrl(componentsPath))
    } else {
      componentsModule = await import(`${pluginName}/components`)
    }

const lightDefaultDarkmodeScript = `
var userPref = localStorage.getItem("theme");
var theme = (userPref === "dark" || userPref === "light") ? userPref : "light";
document.documentElement.setAttribute("saved-theme", theme);

var applyBodyTheme = function(t) {
  if (document.body) {
    document.body.classList.remove("theme-dark", "theme-light");
    document.body.classList.add("theme-" + t);
  }
};

var emitThemeChange = function(t) {
  var n = new CustomEvent("themechange", { detail: { theme: t } });
  document.dispatchEvent(n);
};

var toggleTheme = function() {
  var next = document.documentElement.getAttribute("saved-theme") === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("saved-theme", next);
  localStorage.setItem("theme", next);
  applyBodyTheme(next);
  emitThemeChange(next);
};

var setupThemeToggle = function() {
  var current = document.documentElement.getAttribute("saved-theme") || "light";
  applyBodyTheme(current);

  var buttons = document.getElementsByClassName("darkmode");
  for (var i = 0; i < buttons.length; i++) {
    var btn = buttons[i];
    btn.removeEventListener("click", toggleTheme);
    btn.addEventListener("click", toggleTheme);
    if (typeof window.addCleanup === "function") {
      window.addCleanup(function() { btn.removeEventListener("click", toggleTheme); });
    }
  }
};

document.addEventListener("nav", setupThemeToggle);
document.addEventListener("render", setupThemeToggle);
document.addEventListener("DOMContentLoaded", setupThemeToggle);
`

    const componentEntries = Object.entries(manifest.components)
    const registeredComponents: Record<string, QuartzComponentConstructor> = {}
    for (const [exportName, componentManifest] of componentEntries) {
      let component = componentsModule[exportName]
      if (!component) {
        console.warn(
          `Component "${exportName}" declared in manifest but not found in ${pluginName}/components`,
        )
        continue
      }

      if (pluginName === "@quartz-community/darkmode" || exportName === "Darkmode") {
        const rawCtor = component as QuartzComponentConstructor
        const wrappedCtor: QuartzComponentConstructor = (opts?: any) => {
          const comp = (rawCtor as any)(opts)
          if (comp) {
            comp.beforeDOMLoaded = lightDefaultDarkmodeScript
          }
          return comp
        }
        ;(wrappedCtor as any).beforeDOMLoaded = lightDefaultDarkmodeScript
        try {
          const rawInstance = (rawCtor as any)()
          if (rawInstance) {
            rawInstance.beforeDOMLoaded = lightDefaultDarkmodeScript
            if (rawInstance.css) (wrappedCtor as any).css = rawInstance.css
          }
        } catch {}
        component = wrappedCtor
      }
      registeredComponents[exportName] = component as QuartzComponentConstructor

      // Register under the fully-qualified key (pluginName/exportName)
      componentRegistry.register(
        `${pluginName}/${exportName}`,
        component as QuartzComponentConstructor,
        pluginName,
        componentManifest as ComponentManifest,
      )

      // Also register under just the export name (e.g. "Footer", "NotePropertiesComponent")
      // so buildLayoutForEntries can find it via PascalCase conversion of plugin name
      if (!componentRegistry.get(exportName)) {
        componentRegistry.register(
          exportName,
          component as QuartzComponentConstructor,
          pluginName,
          componentManifest as ComponentManifest,
        )
      }
    }

    // If plugin has exactly one component, also register under just the plugin name
    // (e.g. "footer", "note-properties") for direct kebab-case lookup
    if (componentEntries.length === 1) {
      const [exportName] = componentEntries[0]
      const component = registeredComponents[exportName]
      if (component && !componentRegistry.get(pluginName)) {
        componentRegistry.register(
          pluginName,
          component as QuartzComponentConstructor,
          pluginName,
          componentEntries[0][1] as ComponentManifest,
        )
      }
    }
  } catch (err) {
    console.error("ComponentLoader error for " + pluginName + ":", err)
    if (manifest.components && Object.keys(manifest.components).length > 0) {
      console.warn(`Plugin "${pluginName}" declares components but failed to load them`)
    }
  }
}
