Class dc.Demo.PersistentClass Extends %Persistent
{

/// Description
Property Test As %VarString;

Storage Default
{
<Data name="PersistentClassDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>Test</Value>
</Value>
</Data>
<DataLocation>^dc.Demo.PersistentClassD</DataLocation>
<DefaultData>PersistentClassDefaultData</DefaultData>
<IdLocation>^dc.Demo.PersistentClassD</IdLocation>
<IndexLocation>^dc.Demo.PersistentClassI</IndexLocation>
<StreamLocation>^dc.Demo.PersistentClassS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
