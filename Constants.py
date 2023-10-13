class Config:
    TRAIT_CODE_BEGINNING = (
        "using System; \n"
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
        "\t\t public static void init() \n\t\t{"
    )

    EFFECTS_CODE_BEGINNING = TRAIT_CODE_BEGINNING.replace("Traits", "Effects")

    TRAIT_CODE_ENDING = (
        "\n\n"
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
        "\n\t\t}"
        "\n"
        "\t}"
        "\n"
        "}"
    )

    ATTACK_ACTION_BEGGINING = (
        "(BaseSimObject pSelf, BaseSimObject pTarget, WorldTile pTile)" "\n" "\t\t{"
    )
    ATTACK_ACTION_ENDING = "\n\n\t\t}" "\n\t\t//HERE GOES FUNCTIONS"

    PROJECTILE_CODE_BEGINNING = (
        EFFECTS_CODE_BEGINNING.replace("Traits", "NewProjectiles : MonoBehavior")
        + "\n\t\t\tloadProjectiles();"
        "\n\t\t}"
        "\n\t\t public static void loadProjectiles() \n\t\t{"
    )
    PROJECTILE_CODE_ENDING = "\n\t\t}" "\n" "\t}" "\n" "}"

    # A wee bit o'code
    ASSORTED_MAGIC_CODE = (
        "\n"
        "\t\t\tif(pTarget != null)"
        "\n\t\t\t{"
        "\n\t\t\t\tif (Toolbox.randomChance(0.2f))"
        "\n\t\t\t\t{"
        '\n\t\t\t\t\tMapBox.instance.dropManager.spawn(pTile, "fire", 4f, -1f);'
        '\n\t\t\t\t\tMapBox.instance.dropManager.spawn(pTile, "acid", 4f, -1f);'
        '\n\t\t\t\t\tMapBox.instance.dropManager.spawn(pTile, "fire", 4f, -1f);'
        "\n\t\t\t\t}"
        "\n\t\t\t\tif (Toolbox.randomChance(0.01f))"
        "\n\t\t\t\t{"
        "\n\t\t\t\t\tActionLibrary.castCurses(null, pTarget, null);"
        "\n\t\t\t\t}"
        "\n\t\t\t\tif (Toolbox.randomChance(0.01f))"
        "\n\t\t\t\t{"
        "\n\t\t\t\t\tActionLibrary.addFrozenEffectOnTarget(null, pTarget, null); //Notice how this uses pTarget"
        "\n\t\t\t\t}"
        "\n\t\t\t\tif (Toolbox.randomChance(0.05f))"
        "\n\t\t\t\t{"
        "\n\t\t\t\t\tActionLibrary.castShieldOnHimself(null, pSelf, null); //Notice how this uses pSelf"
        "\n\t\t\t\t}"
        "\n\t\t\t\tif (Toolbox.randomChance(0.04f))"
        "\n\t\t\t\t{"
        "\n\t\t\t\t\tActionLibrary.teleportRandom(null, pTarget, null);"
        "\n\t\t\t\t}"
        "\n\t\t\t\tif (Toolbox.randomChance(0.04f))"
        "\n\t\t\t\t{"
        "\n\t\t\t\t\tActionLibrary.castLightning(null, pTarget, null);"
        "\n\t\t\t\t}"
        "\n\t\t\t\tif (Toolbox.randomChance(0.004f))"
        "\n\t\t\t\t{"
        '\n\t\t\t\t\tEffectsLibrary.spawn("fx_meteorite", pTarget.currentTile, "meteorite_disaster", null, 0f, -1f, -1f); //launches a metorite on the target title the -1 is to "calculate" the position its basically like sayinng null or dont count this param'
        '\n\t\t\t\t\tpSelf.a.addStatusEffect("invincible", 2f); //You dont want the guy who launched this to die so yea'
        "\n\t\t\t\t}"
        "\n\t\t\t\tif (Toolbox.randomChance(0.001f))"
        "\n\t\t\t\t{"
        '\n\t\t\t\t\tEffectsLibrary.spawn("fx_fireball_explosion", pTarget.a.currentTile, null, null, 0f, -1f, -1f);'
        '\n\t\t\t\t\tMapAction.damageWorld(pSelf.currentTile, 2, AssetManager.terraform.get("grenade"), null);'
        '\n\t\t\t\t\tpSelf.a.addStatusEffect("invincible", 2f); //You dont want the guy who launched this to die so yea'
        "\n\t\t\t\t}"
        "\n\t\t\t}"
    )

    PROJECTILE_ACTION_BEGGINING = (
        "\n"
        "\t\t\tif(pTarget != null)"
        "\n\t\t\t{"
        "\n\t\t\t\tif (Toolbox.randomChance(0.2f))"
        "\n\t\t\t\t{"
        "\n\t\t\t\t\tVector2Int pos = pTile.pos; // Position of the Ptile as a Vector 2"
        "\n\t\t\t\t\tfloat pDist = Vector2.Distance(pTarget.currentPosition, pos); // the distance between the target and the pTile"
        "\n\t\t\t\t\tVector3 newPoint = Toolbox.getNewPoint(pSelf.currentPosition.x, pSelf.currentPosition.y, (float)pos.x, (float)pos.y, pDist, true); // the Point of the projectile launcher "
        "\n\t\t\t\t\tVector3 newPoint2 = Toolbox.getNewPoint(pTarget.currentPosition.x, pTarget.currentPosition.y, (float)pos.x, (float)pos.y, pTarget.a.stats[S.size], true);"
    )

    PROJECTILE_ACTION_ENDING = "\n\t\t\t\t}"

    EFFECTS_CODE_ENDING = (
        TRAIT_CODE_ENDING.replace(
            'localizedText.Add("trait_" + id, id);', "localizedText.Add(name, id);"
        )
        .replace(
            'localizedText.Add("trait_" + id + "_info", description);',
            "localizedText.Add(description, description);",
        )
        .replace(
            "addTraitToLocalizedLibrary(string id, string description)",
            "localizeStatus(string id, string name, string description)",
        )
    )

    MAIN_CODE = (
        "using System; \n"
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
