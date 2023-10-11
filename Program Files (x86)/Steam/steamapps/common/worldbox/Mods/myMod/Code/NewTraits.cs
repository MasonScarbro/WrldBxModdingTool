using System; 
using System.Threading; 
using NCMS; 
using UnityEngine; 
using ReflectionUtility; 
using System.Text; 
using System.Collections.Generic; 
using System.Linq; 
using System.Text; 
using ai; 

namespace MyMod 
{
	 class Traits 
	{
		 public static void init() 
		{
		ActorTrait randoTrait = new ActorTrait();
		randoTrait.id = "randoTrait";
		randoTrait.path_icon = "ui/icons/achievements/achievements_thedemon";
		randoTrait.base_stats[S.damage] += 0f;
		randoTrait.base_stats[S.health] += 0f;
		randoTrait.base_stats[S.attack_speed] += 0f;
		randoTrait.base_stats[S.critical_chance] += 0.0f;
		randoTrait.base_stats[S.speed] += 0f;
		randoTrait.base_stats[S.dodge] += 0.0f;
		randoTrait.base_stats[S.accuracy] += 0f;
		randoTrait.base_stats[S.range] += 0f;
		randoTrait.base_stats[S.scale] += 0.0f;
		randoTrait.base_stats[S.intelligence] += 0f;
		randoTrait.base_stats[S.warfare] += 0f;
		randoTrait.base_stats[S.stewardship] += 0f;
		//randoTraitAttackFunction
		randoTrait.action_attack_target = new AttackAction(ActionLibrary.addBurningEffectOnTarget);
		AssetManager.traits.add(randoTrait);
		PlayerConfig.unlockTrait(randoTrait.id);
		addTraitToLocalizedLibrary(randoTrait.id, "This Is My First Trait!");


		}

 		//OTHER FUNCTIONS GO HERE i.e custom death effects etc. 

 		//HERE GOES FUNCTIONS
		public static void addTraitToLocalizedLibrary(string id, string description)
		{

			string language = Reflection.GetField(LocalizedTextManager.instance.GetType(), LocalizedTextManager.instance, "language") as string;
			Dictionary<string, string> localizedText = Reflection.GetField(LocalizedTextManager.instance.GetType(), LocalizedTextManager.instance, "localizedText") as Dictionary<string, string>;
			localizedText.Add("trait_" + id, id);
			localizedText.Add("trait_" + id + "_info", description);
		}
	}
}