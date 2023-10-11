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
	 class Effects 
	{
		 public static void init() 
		{
		StatusEffect randoEffect = new StatusEffect();
		randoEffect.id = "randoEffect";
		randoEffect.duration = 0f;
		randoEffect.base_stats[S.damage] += 0f;
		randoEffect.base_stats[S.health] += 0f;
		randoEffect.base_stats[S.attack_speed] += 0f;
		randoEffect.base_stats[S.critical_chance] += 0.0f;
		randoEffect.base_stats[S.speed] += 0f;
		randoEffect.base_stats[S.dodge] += 0.0f;
		randoEffect.base_stats[S.accuracy] += 0f;
		randoEffect.base_stats[S.range] += 0f;
		randoEffect.base_stats[S.knockback_reduction] += 0.0f;
		randoEffect.base_stats[S.knockback] += 0.0f;
		randoEffect.path_icon = "ui/icons/achievements/achievements_thedemon";
		randoEffect.name = "status_title_randoEffect";
		AssetManager.status.add(randoEffect);
		addTraitToLocalizedLibrary(randoEffect.id, "This Is My First Trait!");


		}

 		//OTHER FUNCTIONS GO HERE i.e custom death effects etc. 

 		//HERE GOES FUNCTIONS
		public static void localizeStatus(string id, string name, string description)
		{

			string language = Reflection.GetField(LocalizedTextManager.instance.GetType(), LocalizedTextManager.instance, "language") as string;
			Dictionary<string, string> localizedText = Reflection.GetField(LocalizedTextManager.instance.GetType(), LocalizedTextManager.instance, "localizedText") as Dictionary<string, string>;
			localizedText.Add(name, id);
			localizedText.Add(description, description);
		}
	}
}