using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class Entities : MonoBehaviour
{
    [Header("Static Data")]

    public string entityName;

    [Header("Irregular Entities")]

    public SaveSystem saveSystem;

    public bool irregular = false;
    public IrregularType irregularType;
    public enum IrregularType
    {
        Null,
        Save,
        StuckDoor
    }

    [Header("Handling Entity Class")]    
    public EntityClass entityClass;

    public enum EntityClass
    {
        Door,
        Key,
        Person,
        Static
    }

    [Header("Assignments - UI")]

    public TextMeshProUGUI mainTextObject;

    [Header("Entity - Door")]
    public bool hasKey = false;
    public DoorMaterial doorMaterial;
    public GameObject requiredKey;

    public enum DoorMaterial
    {
        Wood,
        Stone,
        Metal,
        Reinforced
    }

    [Header("Entity - Key")]
    public Entities doorInstance;

    [Header("Entity - Person")]
    public string[] paragraphs = new string[1];

    [Header("Entity - Static")]
    public bool shouldDisapear = false;
    public bool shouldMove = false;
    public float moveSpeed = 1;
    public Transform desiredMovePos;
    public Material material;
    public enum Material
    {
        Synthetic,
        Wood,
        Plastic,
        Metal,
        Skin,
        Glass
    }


    void OnMouseDown()
    {
        if (!irregular)
        {
            if(entityClass == EntityClass.Door)
            {
                DoorEntityBehaviour(entityName, hasKey);
            }
            if(entityClass == EntityClass.Key)
            {
                KeyEntityBehaviour(entityName);
            }
            if(entityClass == EntityClass.Person)
            {
                PersonEntityBehaviour(entityName);
            }
            if(entityClass == EntityClass.Static)
            {
                StaticEntityBehaviour(entityName, material);
            }
        }
        else
        {
            if(irregularType == IrregularType.Null)
            {
                DefaultEntityBehaviour(entityname);
            }
            if(irregularType == IrregularType.Save)
            {
                SaveEntityBehaviour();
            }
            if(irregularType == IrregularType.StuckDoor)
            {
                StuckDoorEntityBehaviour();
            }
        }
    }

    public void DefaultEntityBehaviour(string name)
    {
        mainTextObject.text = "It's a " + name + ".";
    }

    //Custom Entity Classes

    public void DoorEntityBehaviour(string name, bool isunlocked)
    {
        if(isunlocked)
        {
            mainTextObject.text = "You unlocked the " + name + ".";
            gameObject.SetActive(false);
        }
        else
        {
            mainTextObject.text = "The " + name + " is locked...";
        }
    }

    public void KeyEntityBehaviour(string name)
    {
        mainTextObject.text = "You pocketed a " + name + "!";
        doorInstance.hasKey = true;
        gameObject.SetActive(false);
    }

    public void PersonEntityBehaviour(string name)
    {
        mainTextObject.text = paragraphs[1];
    }
    public void StaticEntityBehaviour(string name, Material sMaterial)
    {
        mainTextObject.text = "It's a " + name + "...";
        Debug.Log(sMaterial);

        if (shouldMove)
        {
            EntityMoveController(desiredMovePos);
        }
        if (shouldDisapear)
        {
            gameObject.SetActive(false);
        }
    }
    public void EntityMoveController(Transform targetPos, float speed)
    {
        //lerp to targetPos over time
    }



    //Irregulars
    public void SaveEntityBehaviour()
    {
        saveSystem.Save();
    }
    public void StuckDoorEntityBehaviour()
    {

    }
}
