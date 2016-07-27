#coding:utf-8
""" 
Created on 2012-1-10 
Create a xml document 
@author: xiaojay 
"""
from const import *
from xml.dom import minidom 
def addChildNode(doc,Node,Tag,TextNode):
    ChildNode = doc.createElement(Tag) 
    ChildNode.appendChild(doc.createTextNode(TextNode)) 
    Node.appendChild(ChildNode) 
    return Node

def addUtil(doc,Node,newNode):
    Node = addChildNode(doc,Node,"a:ObjectID",newNode["ObjectID"])
    Node = addChildNode(doc,Node,"a:Name",newNode["Name"])
    Node = addChildNode(doc,Node,"a:Code",newNode["Code"])
    Node = addChildNode(doc,Node,"a:CreationDate",newNode["CreationDate"])
    Node = addChildNode(doc,Node,"a:Creator",newNode["Creator"])
    Node = addChildNode(doc,Node,"a:ModificationDate",newNode["ModificationDate"])
    Node = addChildNode(doc,Node,"a:Modifier",newNode["Modifier"])
    return Node
    
def addColumn(doc,newColumn): 
    Column = doc.createElement("o:Column") 
    Column.setAttribute("Id", newColumn["Id"]) 
    newDict = {"ObjectID":"89E2AE4C-EDAB-48C9-BA77-F0C2B9F551FE","Name":"name","Code":"name","CreationDate":"1462418188","Creator":"zhouxy","ModificationDate":"1462418188","Modifier":"zhouxy"}
    Column = addUtil(doc,Column,newDict)

    Column = addChildNode(doc,Column,"a:DataType",newColumn["DataType"])
    Column = addChildNode(doc,Column,"a:Identity",newColumn["Identity"])
    Column = addChildNode(doc,Column,"a:Column.Mandatory",newColumn["Mandatory"])
      
    return Column

def addKey(doc,newKey): 
    Key = doc.createElement("o:Key") 
    Key.setAttribute("Id", newKey["Id"]) 
    newDict = {"ObjectID":"81F15C15-F9B5-4E75-A12B-099E582FBCE1","Name":"Key_1","Code":"Key_1","CreationDate":"1462418188","Creator":"zhouxy","ModificationDate":"1462418188","Modifier":"zhouxy"}
    Key = addUtil(doc,Key,newDict)
      
    Columns = doc.createElement("c:Key.Columns") 
    Column = doc.createElement("o:Column") 
    Column.setAttribute("Ref", newKey["Ref"]) 
    Columns.appendChild(Column) 
    Key.appendChild(Columns) 
    return Key

def addPrimaryKey(doc,KeyId): 
    PrimaryKey = doc.createElement("c:PrimaryKey") 
    Key = doc.createElement("o:Key") 
    Key.setAttribute("Ref", KeyId)       
    PrimaryKey.appendChild(Key) 
    return PrimaryKey

    
def addDBMS(doc):
    DBMS = doc.createElement("c:DBMS") 
    Shortcut = doc.createElement("o:Shortcut") 
    Shortcut.setAttribute("Id", "o3") 
    newShortcut = DBMS_Shortcut
    Shortcut = addUtil(doc,Shortcut,newShortcut)
    
    TargetStereotype = doc.createElement("a:TargetStereotype") 
    Shortcut.appendChild(TargetStereotype) 
    
    Shortcut = addChildNode(doc,Shortcut,"a:TargetID",newShortcut["TargetID"])
    Shortcut = addChildNode(doc,Shortcut,"a:TargetClassID",newShortcut["TargetClassID"])
    DBMS.appendChild(Shortcut) 
    return DBMS
def addPhysicalDiagrams(doc,newPhysicalDiagram):
    PhysicalDiagrams = doc.createElement("c:PhysicalDiagrams") 
    PhysicalDiagram = doc.createElement("o:PhysicalDiagram") 
    PhysicalDiagram.setAttribute("Id", "o4") 
    newPhysicalDiagram = newPhysicalDiagram
    PhysicalDiagram = addUtil(doc,PhysicalDiagram,newPhysicalDiagram)
    
    PhysicalDiagram = addChildNode(doc,PhysicalDiagram,"a:DisplayPreferences",newPhysicalDiagram["DisplayPreferences"])
    PhysicalDiagram = addChildNode(doc,PhysicalDiagram,"a:PaperSize","(8268, 11693)")
    PhysicalDiagram = addChildNode(doc,PhysicalDiagram,"a:PageMargins","((315,354), (433,354))")
    PhysicalDiagram = addChildNode(doc,PhysicalDiagram,"a:PageOrientation","1")
    PhysicalDiagram = addChildNode(doc,PhysicalDiagram,"a:PaperSource","15")
    
    PhysicalDiagrams.appendChild(PhysicalDiagram) 
    return PhysicalDiagrams

def addDefaultDiagram(doc):
    DefaultDiagram = doc.createElement("c:DefaultDiagram") 
    PhysicalDiagram = doc.createElement("o:PhysicalDiagram") 
    PhysicalDiagram.setAttribute("Ref", "o4") 
    DefaultDiagram.appendChild(PhysicalDiagram) 
    return DefaultDiagram

def addTables(doc):
    Tables = doc.createElement("c:Tables") 
    Table = doc.createElement("o:Table") 
    Table.setAttribute("Id", "o7") 
    Table = addUtil(doc,Table,newTable)
    
    TotalSavingCurrency = doc.createElement("a:TotalSavingCurrency") 
    Table.appendChild(TotalSavingCurrency) 
    newColumn = {"Id":"o8","DataType":"int","Mandatory":"1","Identity":""}
    Columns = doc.createElement("c:Columns") 
    Column = addColumn(doc,newColumn)
    Columns.appendChild(Column) 
    Table.appendChild(Columns)
    
    newKey = {"Id":"o9","Ref":"o8"}
    Keys = doc.createElement("c:Keys") 
    Key = addKey(doc,newKey)
    Keys.appendChild(Key) 
    Table.appendChild(Keys)
    PrimaryKey = addPrimaryKey(doc,"o9")
    Table.appendChild(PrimaryKey)
    Tables.appendChild(Table) 
    return Tables
def addReferences(doc):
    References = doc.createElement("c:References") 
    Reference = doc.createElement("c:Reference") 
    Reference.setAttribute("Id", "o26")
    newReference = {"Id":"o7","ObjectID":"741E15F8-CE6C-4E31-BD1A-605E89B23A64","Name":"ID","Code":"ID","CreationDate":"","Creator":"Creator","ModificationDate":"111","Modifier":"Modifier"}
    Reference = addUtil(doc,Reference,newReference)
    Reference = addChildNode(doc,Reference,"c:Cardinality","0..*")
    Reference = addChildNode(doc,Reference,"c:UpdateConstraint","1")
    Reference = addChildNode(doc,Reference,"c:DeleteConstraint","1")

    ParentTable = doc.createElement("c:ParentTable") 
    Table = doc.createElement("c:Table") 
    Table.setAttribute("Ref", "o3")
    ParentTable.appendChild(Table) 
    Reference.appendChild(ParentTable) 

    ChildTable = doc.createElement("c:ChildTable") 
    Table = doc.createElement("c:Table") 
    Table.setAttribute("Ref", "o3")
    ChildTable.appendChild(Table) 
    Reference.appendChild(ChildTable) 

    ParentKey = doc.createElement("c:ParentKey") 
    Key = doc.createElement("c:Key") 
    Key.setAttribute("Ref", "o3")
    ParentKey.appendChild(Key) 
    Reference.appendChild(ParentKey) 

    Joins = doc.createElement("c:Joins") 
    ReferenceJoin = doc.createElement("c:ReferenceJoin") 
    ReferenceJoin.setAttribute("Id", "o3")
    newReferenceJoin = {"Id":"o7","ObjectID":"741E15F8-CE6C-4E31-BD1A-605E89B23A64","Name":"ID","Code":"ID","CreationDate":"","Creator":"Creator","ModificationDate":"111","Modifier":"Modifier"}
    ReferenceJoin = addUtil(doc,ReferenceJoin,newReferenceJoin)
    
    Object1 = doc.createElement("c:Object1") 
    Column = doc.createElement("c:Column") 
    Column.setAttribute("Ref", "o3")
    Object1.appendChild(Column) 
    ReferenceJoin.appendChild(Object1) 
    
    Object2 = doc.createElement("c:Object2") 
    Column = doc.createElement("c:Column") 
    Column.setAttribute("Ref", "o3")
    Object2.appendChild(Column) 
    ReferenceJoin.appendChild(Object2) 
    
    Joins.appendChild(ReferenceJoin) 
    Reference.appendChild(Joins) 

    References.appendChild(Reference)
    return References

    
def addDefaultGroups(doc):
    DefaultGroups = doc.createElement("c:DefaultGroups") 
    Group = doc.createElement("o:Group") 
    Group.setAttribute("Id", "o5")
    #newGroup = newGroup
    Group = addUtil(doc,Group,newGroup)
    DefaultGroups.appendChild(Group)
    return DefaultGroups

def addTargetModels(doc):
    TargetModels = doc.createElement("c:TargetModels") 
    TargetModel = doc.createElement("o:TargetModel") 
    TargetModel.setAttribute("Id", "o6")
    #newTargetModel = newTargetModel
    TargetModel = addUtil(doc,TargetModel,newTargetModel)
    TargetModel = addChildNode(doc,TargetModel,"a:TargetModelURL",newTargetModel["TargetModelURL"])
    TargetModel = addChildNode(doc,TargetModel,"a:TargetModelID",newTargetModel["TargetModelID"])
    TargetModel = addChildNode(doc,TargetModel,"a:TargetModelClassID",newTargetModel["TargetModelClassID"])

    SessionShortcuts = doc.createElement("c:SessionShortcuts") 
    Shortcut = doc.createElement("o:Shortcut") 
    Shortcut.setAttribute("Ref", "o3")
    SessionShortcuts.appendChild(Shortcut) 
    TargetModel.appendChild(SessionShortcuts) 

    TargetModels.appendChild(TargetModel)
    return TargetModels

def createModel():
    doc = minidom.Document() 
    doc.appendChild(doc.createComment("do not edit this file")) 
    Model = doc.createElement("Model") 
    Model.setAttribute("xmlns:a", "attribute")
    Model.setAttribute("xmlns:c", "collection")
    Model.setAttribute("xmlns:o", "object")
    
    RootObject = doc.createElement("o:RootObject") 
    RootObject.setAttribute("Id", "o1") 

    Children = doc.createElement("c:Children") 
    o_Model = doc.createElement("o:Model") 
    o_Model.setAttribute("Id", "o2") 
    newo_Model = newModel
    o_Model = addUtil(doc,o_Model,newo_Model)
    o_Model = addChildNode(doc,o_Model,"a:PackageOptionsText",PackageOptionsText)
    o_Model = addChildNode(doc,o_Model,"a:ModelOptionsText",ModelOptionsText)
#    o_Model = addChildNode(doc,o_Model,"a:RepositoryInformation","RepositoryInformation")
    o_Model = addChildNode(doc,o_Model,"a:ExternalDependenciesText","ExternalDependenciesText")
    
    DBMS = addDBMS(doc)
    o_Model.appendChild(DBMS) 

    PhysicalDiagrams = addPhysicalDiagrams(doc,newPhysicalDiagram)
    o_Model.appendChild(PhysicalDiagrams) 

    DefaultDiagram = addDefaultDiagram(doc)
    o_Model.appendChild(DefaultDiagram) 

    Tables = addTables(doc)
    o_Model.appendChild(Tables) 

#    References = addReferences(doc)
#    o_Model.appendChild(References) 

    DefaultGroups = addDefaultGroups(doc)
    o_Model.appendChild(DefaultGroups) 

    TargetModels = addTargetModels(doc)
    o_Model.appendChild(TargetModels) 

    Children.appendChild(o_Model) 
    RootObject.appendChild(Children) 

    Model.appendChild(RootObject) 

    doc.appendChild(Model) 
    f = file("Model.pdm","w") 
    doc.writexml(f) 
    f.close() 
    f = open("Model.pdm","r")
    content = f.read()
    f.close()
    f = open("Model.pdm","w")
    head = """<?xml version="1.0" encoding="UTF-8"?>
<?PowerDesigner AppLocale="UTF16" ID="{6830E4D9-BAD9-4C74-A32D-15EE6F501E74}" Label="" LastModificationDate="1462430460" Name="Physical Data _1" Objects="50" Symbols="0" Target="ORACLE Version 10g" Type="{CDE44E21-9669-11D1-9914-006097355D9B}" signature="PDM_DATA_MODEL_XML" version="15.3.0.3248"?>
"""
    f.write("%s%s"%(head,content.replace('&amp;','&').replace('<?xml version="1.0" ?>','')))
    f.close()
createModel()
