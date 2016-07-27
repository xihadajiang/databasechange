""" 
Created on 2012-1-10 
Create a xml document 
@author: xiaojay 
"""

from xml.dom import minidom 

def addUtil(doc,Node,newNode):
    ObjectID = doc.createElement("a:ObjectID") 
    ObjectID.appendChild(doc.createTextNode(newNode["ObjectID"])) 
    Node.appendChild(ObjectID) 

    Name = doc.createElement("a:Name") 
    Name.appendChild(doc.createTextNode(newNode["Name"])) 
    Node.appendChild(Name) 
    
    Code = doc.createElement("a:Code") 
    Code.appendChild(doc.createTextNode(newNode["Code"])) 
    Node.appendChild(Code) 
      
    CreationDate = doc.createElement("a:CreationDate") 
    CreationDate.appendChild(doc.createTextNode(newNode["CreationDate"])) 
    Node.appendChild(CreationDate) 
      
    Creator = doc.createElement("a:Creator") 
    Creator.appendChild(doc.createTextNode(newNode["Creator"])) 
    Node.appendChild(Creator) 
      
    ModificationDate = doc.createElement("a:ModificationDate") 
    ModificationDate.appendChild(doc.createTextNode(newNode["ModificationDate"])) 
    Node.appendChild(ModificationDate) 
      
    Modifier = doc.createElement("a:Modifier") 
    Modifier.appendChild(doc.createTextNode(newNode["Modifier"])) 
    Node.appendChild(Modifier) 
    
    return Node
def addColumn(doc,newColumn): 
    Column = doc.createElement("o:Column") 
    Column.setAttribute("Id", newColumn["Id"]) 
    newDict = {"Id":"o7","ObjectID":"741E15F8-CE6C-4E31-BD1A-605E89B23A64","Name":"ID","Code":"ID","CreationDate":"","Creator":"Creator","ModificationDate":"111","Modifier":"Modifier"}
    Column = addUtil(doc,Column,newDict)

    DataType = doc.createElement("a:DataType") 
    DataType.appendChild(doc.createTextNode(newColumn["DataType"])) 
    Column.appendChild(DataType) 
      
    Identity = doc.createElement("a:Identity") 
    Identity.appendChild(doc.createTextNode(newColumn["Identity"])) 
    Column.appendChild(Identity) 
      
    Mandatory = doc.createElement("a:Column.Mandatory") 
    Mandatory.appendChild(doc.createTextNode(newColumn["Mandatory"])) 
    Column.appendChild(Mandatory) 
    return Column

def addKey(doc,newKey): 
    Key = doc.createElement("o:Key") 
    Key.setAttribute("Id", newKey["Id"]) 
    newDict = {"Id":"o7","ObjectID":"741E15F8-CE6C-4E31-BD1A-605E89B23A64","Name":"ID","Code":"ID","CreationDate":"","Creator":"Creator","ModificationDate":"111","Modifier":"Modifier"}
    Key = addUtil(doc,Key,newDict)
      
    Columns = doc.createElement("a:Key.Columns") 
    Column = doc.createElement("o:Column") 
    Column.setAttribute("Ref", newKey["Ref"]) 
    Columns.appendChild(Column) 
    Key.appendChild(Columns) 
    return Key

def addPrimaryKey(doc): 
    PrimaryKey = doc.createElement("o:PrimaryKey") 
    Key = doc.createElement("o:Key") 
    Key.setAttribute("Ref", "o22")       
    PrimaryKey.appendChild(Key) 
    return PrimaryKey

    
def addDBMS(doc):
    DBMS = doc.createElement("c:DBMS") 
    Shortcut = doc.createElement("o:Shortcut") 
    Shortcut.setAttribute("Id", "o3") 
    newShortcut = {"Id":"o7","ObjectID":"741E15F8-CE6C-4E31-BD1A-605E89B23A64","Name":"ID","Code":"ID","CreationDate":"","Creator":"Creator","ModificationDate":"111","Modifier":"Modifier"}
    Shortcut = addUtil(doc,Shortcut,newShortcut)
    
    TargetStereotype = doc.createElement("a:TargetStereotype") 
    Shortcut.appendChild(TargetStereotype) 
    
    TargetID = doc.createElement("a:TargetID") 
    TargetID.appendChild(doc.createTextNode("TargetID")) 
    Shortcut.appendChild(TargetID) 
    
    TargetClassID = doc.createElement("a:TargetClassID") 
    TargetClassID.appendChild(doc.createTextNode("TargetClassID")) 
    Shortcut.appendChild(TargetClassID) 
    
    DBMS.appendChild(Shortcut) 
    return DBMS
def addPhysicalDiagrams(doc):
    PhysicalDiagrams = doc.createElement("c:PhysicalDiagrams") 
    PhysicalDiagram = doc.createElement("o:PhysicalDiagram") 
    PhysicalDiagram.setAttribute("Id", "o4") 
    newPhysicalDiagram = {"Id":"o7","ObjectID":"741E15F8-CE6C-4E31-BD1A-605E89B23A64","Name":"ID","Code":"ID","CreationDate":"","Creator":"Creator","ModificationDate":"111","Modifier":"Modifier"}
    PhysicalDiagram = addUtil(doc,PhysicalDiagram,newPhysicalDiagram)
    
    DisplayPreferences = doc.createElement("a:DisplayPreferences") 
    DisplayPreferences.appendChild(doc.createTextNode("DisplayPreferences")) 
    PhysicalDiagram.appendChild(DisplayPreferences) 
    
    PaperSize = doc.createElement("a:PaperSize") 
    PaperSize.appendChild(doc.createTextNode("(8268, 11693)")) 
    PhysicalDiagram.appendChild(PaperSize) 
    
    PageMargins = doc.createElement("a:PageMargins") 
    PageMargins.appendChild(doc.createTextNode("((315,354), (433,354))")) 
    PhysicalDiagram.appendChild(PageMargins) 
    
    PageOrientation = doc.createElement("a:PageOrientation") 
    PageOrientation.appendChild(doc.createTextNode("1")) 
    PhysicalDiagram.appendChild(PageOrientation) 
    
    PaperSource = doc.createElement("a:PaperSource") 
    PaperSource.appendChild(doc.createTextNode("7")) 
    PhysicalDiagram.appendChild(PaperSource) 
    
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
    Table.setAttribute("Id", "o9") 
    newTable = {"Id":"o7","ObjectID":"741E15F8-CE6C-4E31-BD1A-605E89B23A64","Name":"ID","Code":"ID","CreationDate":"","Creator":"Creator","ModificationDate":"111","Modifier":"Modifier"}
    Table = addUtil(doc,Table,newTable)
    
    TotalSavingCurrency = doc.createElement("a:TotalSavingCurrency") 
    Table.appendChild(TotalSavingCurrency) 
    newColumn = {"Id":"o12","DataType":"int","Mandatory":"1","Identity":""}
    Columns = doc.createElement("a:Columns") 
    Column = addColumn(doc,newColumn)
    Columns.appendChild(Column) 
    Table.appendChild(Columns)
    
    newKey = {"Id":"o11","Ref":"o22"}
    Keys = doc.createElement("a:Keys") 
    Key = addKey(doc,newKey)
    Keys.appendChild(Key) 
    Table.appendChild(Keys)
    PrimaryKey = addPrimaryKey(doc)
    Table.appendChild(PrimaryKey)
    Tables.appendChild(Table) 
    return Tables
def addReferences(doc):
    References = doc.createElement("c:References") 
    Reference = doc.createElement("c:Reference") 
    Reference.setAttribute("Id", "o26")
    newReference = {"Id":"o7","ObjectID":"741E15F8-CE6C-4E31-BD1A-605E89B23A64","Name":"ID","Code":"ID","CreationDate":"","Creator":"Creator","ModificationDate":"111","Modifier":"Modifier"}
    Reference = addUtil(doc,Reference,newReference)

    Cardinality = doc.createElement("c:Cardinality") 
    Cardinality.appendChild(doc.createTextNode("0..*")) 
    Reference.appendChild(Cardinality) 

    UpdateConstraint = doc.createElement("c:UpdateConstraint") 
    UpdateConstraint.appendChild(doc.createTextNode("1")) 
    Reference.appendChild(UpdateConstraint) 

    DeleteConstraint = doc.createElement("c:DeleteConstraint") 
    DeleteConstraint.appendChild(doc.createTextNode("1")) 
    Reference.appendChild(DeleteConstraint) 

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
    Group = doc.createElement("c:Group") 
    Group.setAttribute("Id", "o25")
    newGroup = {"Id":"o7","ObjectID":"741E15F8-CE6C-4E31-BD1A-605E89B23A64","Name":"ID","Code":"ID","CreationDate":"","Creator":"Creator","ModificationDate":"111","Modifier":"Modifier"}
    Group = addUtil(doc,Group,newGroup)
    DefaultGroups.appendChild(Group)
    return DefaultGroups

def addTargetModels(doc):
    TargetModels = doc.createElement("c:TargetModels") 
    TargetModel = doc.createElement("c:TargetModel") 
    TargetModel.setAttribute("Id", "o26")
    newTargetModel = {"Id":"o7","ObjectID":"741E15F8-CE6C-4E31-BD1A-605E89B23A64","Name":"ID","Code":"ID","CreationDate":"","Creator":"Creator","ModificationDate":"111","Modifier":"Modifier"}
    TargetModel = addUtil(doc,TargetModel,newTargetModel)

    TargetModelURL = doc.createElement("c:TargetModelURL") 
    TargetModelURL.appendChild(doc.createTextNode("file:///%_DBMS%/syase1500.xdb")) 
    TargetModel.appendChild(TargetModelURL) 

    TargetModelID = doc.createElement("c:TargetModelID") 
    TargetModelID.appendChild(doc.createTextNode("9F7831CA-9C8B-4764-85FE-EBBCC89134F3")) 
    TargetModel.appendChild(TargetModelID) 

    TargetModelClassID = doc.createElement("c:TargetModelClassID") 
    TargetModelClassID.appendChild(doc.createTextNode("4BA9F647-DAB1-11D1-9944-006097355D9B")) 
    TargetModel.appendChild(TargetModelClassID) 

    SessionShortcuts = doc.createElement("c:SessionShortcuts") 
    Shortcut = doc.createElement("c:Shortcut") 
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
    newo_Model = {"Id":"o7","ObjectID":"741E15F8-CE6C-4E31-BD1A-605E89B23A64","Name":"ID","Code":"ID","CreationDate":"","Creator":"Creator","ModificationDate":"111","Modifier":"Modifier"}
    o_Model = addUtil(doc,o_Model,newo_Model)
    
    PackageOptionsText = doc.createElement("a:PackageOptionsText") 
    PackageOptionsText.appendChild(doc.createTextNode("PackageOptionsText")) 
    o_Model.appendChild(PackageOptionsText) 

    ModelOptionsText = doc.createElement("a:ModelOptionsText") 
    ModelOptionsText.appendChild(doc.createTextNode("ModelOptionsText")) 
    o_Model.appendChild(ModelOptionsText) 

    RepositoryInformation = doc.createElement("a:RepositoryInformation") 
    RepositoryInformation.appendChild(doc.createTextNode("RepositoryInformation")) 
    o_Model.appendChild(RepositoryInformation) 

    ExternalDependenciesText = doc.createElement("a:ExternalDependenciesText") 
    ExternalDependenciesText.appendChild(doc.createTextNode("ExternalDependenciesText")) 
    o_Model.appendChild(ExternalDependenciesText) 
    
    DBMS = addDBMS(doc)
    o_Model.appendChild(DBMS) 

    PhysicalDiagrams = addPhysicalDiagrams(doc)
    o_Model.appendChild(PhysicalDiagrams) 

    DefaultDiagram = addDefaultDiagram(doc)
    o_Model.appendChild(DefaultDiagram) 

    Tables = addTables(doc)
    o_Model.appendChild(Tables) 

    References = addReferences(doc)
    o_Model.appendChild(References) 

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
createModel()
