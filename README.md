# Gaffer
## Modules
## Classes
* BinaryPlugSignal
* BinarySignal
* ErrorSignal
* UnaryPlugSignal
* UnarySignal
* __class__
## Methods
### Range
	def __range( cls, parent ) :

	for child in parent.children() :
		if isinstance( child, cls ) :
			yield child

### RecursiveRange
	def __recursiveNodeRange( cls, parent ) :

	for i in range( 0, len( parent ) ) :
		child = parent[i]
		if isinstance( child, cls ) :
			yield child
		if isinstance( child, Gaffer.Node ) :
			for r in __recursiveNodeRange( cls, child ) :
				yield r

## Functions
### __bool__


__bool__( (GraphComponent)arg1) -> bool :

    C++ signature :
        bool __bool__(Gaffer::GraphComponent {lvalue})
### __contains__


__contains__( (GraphComponent)arg1, (InternedString)arg2) -> bool :

    C++ signature :
        bool __contains__(Gaffer::GraphComponent {lvalue},IECore::InternedString)
### __delitem__


__delitem__( (GraphComponent)arg1, (InternedString)arg2) -> None :

    C++ signature :
        void __delitem__(Gaffer::GraphComponent {lvalue},IECore::InternedString)

__delitem__( (GraphComponent)arg1, (int)arg2) -> None :

    C++ signature :
        void __delitem__(Gaffer::GraphComponent {lvalue},long)
### __eq__


__eq__( (RefCounted)arg1, (object)arg2) -> bool :

    C++ signature :
        bool __eq__(IECore::RefCounted const*,boost::python::api::object)
### __getitem__


__getitem__( (GraphComponent)arg1, (InternedString)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> __getitem__(Gaffer::GraphComponent {lvalue},IECore::InternedString)

__getitem__( (GraphComponent)arg1, (int)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> __getitem__(Gaffer::GraphComponent {lvalue},long)
### __hash__


__hash__( (RefCounted)arg1) -> int :

    C++ signature :
        long __hash__(IECore::RefCounted const*)
### __init__


__init__( (object)arg1 [, (object)name='Node']) -> None :

    C++ signature :
        void __init__(_object* [,std::string='Node'])
### __len__


__len__( (GraphComponent)arg1) -> int :

    C++ signature :
        int __len__(Gaffer::GraphComponent {lvalue})
### __ne__


__ne__( (RefCounted)arg1, (object)arg2) -> bool :

    C++ signature :
        bool __ne__(IECore::RefCounted const*,boost::python::api::object)
### __reduce__

None
### __repr__


__repr__( (GraphComponent)arg1) -> str :

    C++ signature :
        std::string __repr__(Gaffer::GraphComponent const*)
### __setitem__


__setitem__( (GraphComponent)arg1, (InternedString)arg2, (GraphComponent)arg3) -> None :

    C++ signature :
        void __setitem__(Gaffer::GraphComponent {lvalue},IECore::InternedString,Gaffer::GraphComponent {lvalue})
### acceptsChild


acceptsChild( (Node)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(Gaffer::Node,Gaffer::GraphComponent const*)
### acceptsParent


acceptsParent( (Node)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(Gaffer::Node,Gaffer::GraphComponent const*)
### addChild


addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})
### ancestor


ancestor( (GraphComponent)arg1, (TypeId)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> ancestor(Gaffer::GraphComponent {lvalue},IECore::TypeId)
### baseTypeId


baseTypeId([  (TypeId)arg1]) -> TypeId :

    C++ signature :
        IECore::TypeId baseTypeId([ IECore::TypeId])
### baseTypeIds


baseTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list baseTypeIds(IECore::TypeId)
### baseTypeName


baseTypeName() -> str :

    C++ signature :
        char const* baseTypeName()
### childAddedSignal


childAddedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        boost::signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), boost::last_value<void>, int, std::less<int>, boost::function<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*)> > {lvalue} childAddedSignal(Gaffer::GraphComponent {lvalue})
### childRemovedSignal


childRemovedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        boost::signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), boost::last_value<void>, int, std::less<int>, boost::function<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*)> > {lvalue} childRemovedSignal(Gaffer::GraphComponent {lvalue})
### children


children( (GraphComponent)self [, (TypeId)typeId=IECore._IECore.TypeId(110000)]) -> tuple :

    C++ signature :
        boost::python::tuple children(Gaffer::GraphComponent {lvalue} [,IECore::TypeId=IECore._IECore.TypeId(110000)])
### clearChildren


clearChildren( (GraphComponent)arg1) -> None :

    C++ signature :
        void clearChildren(Gaffer::GraphComponent {lvalue})
### collectGarbage


collectGarbage() -> None :

    C++ signature :
        void collectGarbage()
### commonAncestor


commonAncestor( (GraphComponent)self, (GraphComponent)other [, (TypeId)ancestorType=IECore._IECore.TypeId(110000)]) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> commonAncestor(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const* [,IECore::TypeId=IECore._IECore.TypeId(110000)])
### derivedTypeIds


derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)
### descendant


descendant( (GraphComponent)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> descendant(Gaffer::GraphComponent {lvalue},std::string)
### errorSignal


errorSignal( (Node)arg1) -> ErrorSignal :

    C++ signature :
        boost::signal<void (Gaffer::Plug const*, Gaffer::Plug const*, std::string const&), boost::last_value<void>, int, std::less<int>, boost::function<void (Gaffer::Plug const*, Gaffer::Plug const*, std::string const&)> > {lvalue} errorSignal(Gaffer::Node {lvalue})
### fullName


fullName( (GraphComponent)arg1) -> str :

    C++ signature :
        std::string fullName(Gaffer::GraphComponent {lvalue})
### getChild


getChild( (GraphComponent)arg1, (InternedString)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> getChild(Gaffer::GraphComponent {lvalue},IECore::InternedString)
### getName


getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})
### inheritsFrom


inheritsFrom( (str)arg1) -> bool :

    C++ signature :
        bool inheritsFrom(char const*)

inheritsFrom( (TypeId)arg1) -> bool :

    C++ signature :
        bool inheritsFrom(IECore::TypeId)

inheritsFrom( (str)arg1, (str)arg2) -> bool :

    C++ signature :
        bool inheritsFrom(char const*,char const*)

inheritsFrom( (TypeId)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool inheritsFrom(IECore::TypeId,IECore::TypeId)
### isAncestorOf


isAncestorOf( (GraphComponent)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool isAncestorOf(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const*)
### isInstanceOf


isInstanceOf( (Node)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(Gaffer::Node {lvalue},IECore::TypeId)

isInstanceOf( (Node)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(Gaffer::Node {lvalue},char const*)
### isSame


isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)
### items


items( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list items(Gaffer::GraphComponent {lvalue})
### keys


keys( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list keys(Gaffer::GraphComponent {lvalue})
### nameChangedSignal


nameChangedSignal( (GraphComponent)arg1) -> UnarySignal :

    C++ signature :
        boost::signal<void (Gaffer::GraphComponent*), boost::last_value<void>, int, std::less<int>, boost::function<void (Gaffer::GraphComponent*)> > {lvalue} nameChangedSignal(Gaffer::GraphComponent {lvalue})
### numWrappedInstances


numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()
### parent


parent( (GraphComponent)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> parent(Gaffer::GraphComponent {lvalue})
### parentChangedSignal


parentChangedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        boost::signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), boost::last_value<void>, int, std::less<int>, boost::function<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*)> > {lvalue} parentChangedSignal(Gaffer::GraphComponent {lvalue})
### plugDirtiedSignal


plugDirtiedSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        boost::signal<void (Gaffer::Plug*), boost::last_value<void>, int, std::less<int>, boost::function<void (Gaffer::Plug*)> > {lvalue} plugDirtiedSignal(Gaffer::Node {lvalue})
### plugFlagsChangedSignal


plugFlagsChangedSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        boost::signal<void (Gaffer::Plug*), boost::last_value<void>, int, std::less<int>, boost::function<void (Gaffer::Plug*)> > {lvalue} plugFlagsChangedSignal(Gaffer::Node {lvalue})
### plugInputChangedSignal


plugInputChangedSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        boost::signal<void (Gaffer::Plug*), boost::last_value<void>, int, std::less<int>, boost::function<void (Gaffer::Plug*)> > {lvalue} plugInputChangedSignal(Gaffer::Node {lvalue})
### plugSetSignal


plugSetSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        boost::signal<void (Gaffer::Plug*), boost::last_value<void>, int, std::less<int>, boost::function<void (Gaffer::Plug*)> > {lvalue} plugSetSignal(Gaffer::Node {lvalue})
### refCount


refCount( (RefCounted)arg1) -> int :

    C++ signature :
        unsigned long refCount(IECore::RefCounted {lvalue})
### registerType


registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)
### relativeName


relativeName( (GraphComponent)arg1, (GraphComponent)arg2) -> str :

    C++ signature :
        std::string relativeName(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const*)
### removeChild


removeChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void removeChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})
### scriptNode


scriptNode( (Node)arg1) -> object :

    C++ signature :
        Gaffer::ScriptNode* scriptNode(Gaffer::Node {lvalue})
### setChild


setChild( (GraphComponent)arg1, (InternedString)arg2, (GraphComponent)arg3) -> None :

    C++ signature :
        void setChild(Gaffer::GraphComponent {lvalue},IECore::InternedString,Gaffer::GraphComponent {lvalue})
### setName


setName( (GraphComponent)arg1, (InternedString)arg2) -> str :

    C++ signature :
        char const* setName(Gaffer::GraphComponent {lvalue},IECore::InternedString)
### staticTypeId


staticTypeId() -> TypeId :

    C++ signature :
        IECore::TypeId staticTypeId()
### staticTypeName


staticTypeName() -> str :

    C++ signature :
        char const* staticTypeName()
### typeId


typeId( (Node)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(Gaffer::Node {lvalue})
### typeIdFromTypeName


typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)
### typeName


typeName( (Node)arg1) -> str :

    C++ signature :
        char const* typeName(Gaffer::Node {lvalue})
### typeNameFromTypeId


typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)
### values


values( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list values(Gaffer::GraphComponent {lvalue})