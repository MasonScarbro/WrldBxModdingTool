class Config:

    TRAIT_CODE_BEGINNING = ("using System; \n" 
                            "using System.Threading; \n"
                            "using NCMS; \n" 
                            "using UnityEngine; \n"
                            "using ReflectionUtility; \n"
                            "using System.Text; \n"
                            "using System.Collections.Generic; \n"
                            "using System.Linq; \n"
                            "using System.Text; \n"
                            "using ai; \n"
                            "\n"
                            "namespace MyMod \n{"
                            "\n"
                            "\t class Traits \n\t{"
                            "\n"
                            "\t\t public static void init() \n\t\t{")

    EFFECTS_CODE_BEGINNING = TRAIT_CODE_BEGINNING.replace("Traits", "Effects")

    TRAIT_CODE_ENDING = ("\n\n"
                        "\t\t}"
                        "\n"
                        "\n \t\t//OTHER FUNCTIONS GO HERE i.e custom death effects etc. \n"
                        "\n \t\t//HERE GOES FUNCTIONS"
                        "\n"
                        "\t\tpublic static void addTraitToLocalizedLibrary(string id, string description)"
                        "\n\t\t{"
                        "\n"
                        '\n\t\t\tstring language = Reflection.GetField(LocalizedTextManager.instance.GetType(), LocalizedTextManager.instance, "language") as string;'
                        '\n\t\t\tDictionary<string, string> localizedText = Reflection.GetField(LocalizedTextManager.instance.GetType(), LocalizedTextManager.instance, "localizedText") as Dictionary<string, string>;'
                        '\n\t\t\tlocalizedText.Add("trait_" + id, id);'
                        '\n\t\t\tlocalizedText.Add("trait_" + id + "_info", description);'
                        '\n\t\t}'
                        "\n"
                        "\t}"
                        "\n"
                        "}") 

    ATTACK_ACTION_BEGGINING = ("(BaseSimObject pSelf, BaseSimObject pTarget, WorldTile pTile)"
                               "\n"
                               "\t\t{"
                               )
    ATTACK_ACTION_ENDING = "\n\n\t\t}"

    EFFECTS_CODE_ENDING = (TRAIT_CODE_ENDING
                        .replace('localizedText.Add("trait_" + id, id);', 'localizedText.Add(name, id);' )
                        .replace('localizedText.Add("trait_" + id + "_info", description);', 'localizedText.Add(description, description);')
                        .replace('addTraitToLocalizedLibrary(string id, string description)', 'localizeStatus(string id, string name, string description)')) 

    MAIN_CODE = ("using System; \n"
                "using NCMS; \n"
                "using UnityEngine; \n"
                "ReflectionUtility; \n"
                "\n\n"
                "namespace MyMod \n"
                "{ \n"
                "\t[ModEntry] \n"
                "\tclass Main : MonoBehavior \n"
                "\t{"
                "\t\tvoid Awake() \n"
                "\t\t{ \n"
                "\t\t\tTraits.init();\n"
                "\t\t\tEffects.init();\n"
                "\t\t} \n"
                "\t}\n"
                "}"
                )