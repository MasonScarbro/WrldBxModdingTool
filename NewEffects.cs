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
}using System; 
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