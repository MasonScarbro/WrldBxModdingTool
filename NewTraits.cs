using System; 
using NCMS; 
using UnityEngine; 
ReflectionUtility; 


namespace MyMod 
{ 
	[ModEntry] 
	class Main : MonoBehavior 
	{		void Awake() 
		{ 
			Traits.init();
			Effects.init();
		} 
	}
}