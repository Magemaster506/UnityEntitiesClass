using System.Collections;
using System;
using UnityEngine;
using UnityEngine.UI;

public class SaveSystem : MonoBehaviour
{
    [SerializeField] private PlayerData _PlayerData = new PlayerData();

    public void SaveIntoJson()
    {
        string player = HsonUtility.ToJson(_PlayerData);
        System.IO.File.WriteAllText(Application.persistentDataPath + "/PlayerData.json", player)
    }    

}

[System.Serializable]
public class PlayerData{
    public string player_name;
    public float playTime;
}