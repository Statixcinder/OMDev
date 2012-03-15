# Python stubs generated by omniidl from ..\..\..\..\..\idl\COS\CosTradingRepos.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)

# #include "corbaidl.idl"
import corbaidl_idl
_0_CORBA = omniORB.openModule("CORBA")
_0_CORBA__POA = omniORB.openModule("CORBA__POA")
# #include "boxes.idl"
import boxes_idl
_0_CORBA = omniORB.openModule("CORBA")
_0_CORBA__POA = omniORB.openModule("CORBA__POA")
# #include "CosTrading.idl"
import CosTrading_idl
_0_CosTrading = omniORB.openModule("CosTrading")
_0_CosTrading__POA = omniORB.openModule("CosTrading__POA")

#
# Start of module "CosTradingRepos"
#
__name__ = "CosTradingRepos"
_0_CosTradingRepos = omniORB.openModule("CosTradingRepos", r"..\..\..\..\..\idl\COS\CosTradingRepos.idl")
_0_CosTradingRepos__POA = omniORB.openModule("CosTradingRepos__POA", r"..\..\..\..\..\idl\COS\CosTradingRepos.idl")


# interface ServiceTypeRepository
_0_CosTradingRepos._d_ServiceTypeRepository = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosTradingRepos/ServiceTypeRepository:1.0", "ServiceTypeRepository")
omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository:1.0"] = _0_CosTradingRepos._d_ServiceTypeRepository
_0_CosTradingRepos.ServiceTypeRepository = omniORB.newEmptyClass()
class ServiceTypeRepository :
    _NP_RepositoryId = _0_CosTradingRepos._d_ServiceTypeRepository[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil

    
    # typedef ... ServiceTypeNameSeq
    class ServiceTypeNameSeq:
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/ServiceTypeNameSeq:1.0"
        def __init__(self, *args, **kw):
            raise RuntimeError("Cannot construct objects of this type.")
    _d_ServiceTypeNameSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], 0)
    _ad_ServiceTypeNameSeq = (omniORB.tcInternal.tv_alias, ServiceTypeNameSeq._NP_RepositoryId, "ServiceTypeNameSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], 0))
    _tc_ServiceTypeNameSeq = omniORB.tcInternal.createTypeCode(_ad_ServiceTypeNameSeq)
    omniORB.registerType(ServiceTypeNameSeq._NP_RepositoryId, _ad_ServiceTypeNameSeq, _tc_ServiceTypeNameSeq)
    
    # enum PropertyMode
    PROP_NORMAL = omniORB.EnumItem("PROP_NORMAL", 0)
    PROP_READONLY = omniORB.EnumItem("PROP_READONLY", 1)
    PROP_MANDATORY = omniORB.EnumItem("PROP_MANDATORY", 2)
    PROP_MANDATORY_READONLY = omniORB.EnumItem("PROP_MANDATORY_READONLY", 3)
    PropertyMode = omniORB.Enum("IDL:omg.org/CosTradingRepos/ServiceTypeRepository/PropertyMode:1.0", (PROP_NORMAL, PROP_READONLY, PROP_MANDATORY, PROP_MANDATORY_READONLY,))

    _d_PropertyMode  = (omniORB.tcInternal.tv_enum, PropertyMode._NP_RepositoryId, "PropertyMode", PropertyMode._items)
    _tc_PropertyMode = omniORB.tcInternal.createTypeCode(_d_PropertyMode)
    omniORB.registerType(PropertyMode._NP_RepositoryId, _d_PropertyMode, _tc_PropertyMode)
    
    # struct PropStruct
    _0_CosTradingRepos.ServiceTypeRepository.PropStruct = omniORB.newEmptyClass()
    class PropStruct (omniORB.StructBase):
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/PropStruct:1.0"

        _NP_ClassName = "CosTradingRepos.ServiceTypeRepository.PropStruct"

        def __init__(self, name, value_type, mode):
            self.name = name
            self.value_type = value_type
            self.mode = mode
    
    _d_PropStruct  = _0_CosTradingRepos.ServiceTypeRepository._d_PropStruct = (omniORB.tcInternal.tv_struct, PropStruct, PropStruct._NP_RepositoryId, "PropStruct", "name", omniORB.typeMapping["IDL:omg.org/CosTrading/PropertyName:1.0"], "value_type", omniORB.tcInternal.tv_TypeCode, "mode", omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/PropertyMode:1.0"])
    _tc_PropStruct = omniORB.tcInternal.createTypeCode(_d_PropStruct)
    omniORB.registerType(PropStruct._NP_RepositoryId, _d_PropStruct, _tc_PropStruct)
    
    # typedef ... PropStructSeq
    class PropStructSeq:
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/PropStructSeq:1.0"
        def __init__(self, *args, **kw):
            raise RuntimeError("Cannot construct objects of this type.")
    _d_PropStructSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/PropStruct:1.0"], 0)
    _ad_PropStructSeq = (omniORB.tcInternal.tv_alias, PropStructSeq._NP_RepositoryId, "PropStructSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/PropStruct:1.0"], 0))
    _tc_PropStructSeq = omniORB.tcInternal.createTypeCode(_ad_PropStructSeq)
    omniORB.registerType(PropStructSeq._NP_RepositoryId, _ad_PropStructSeq, _tc_PropStructSeq)
    
    # typedef ... Identifier
    class Identifier:
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/Identifier:1.0"
        def __init__(self, *args, **kw):
            raise RuntimeError("Cannot construct objects of this type.")
    _d_Identifier  = omniORB.typeMapping["IDL:omg.org/CosTrading/Istring:1.0"]
    _ad_Identifier = (omniORB.tcInternal.tv_alias, Identifier._NP_RepositoryId, "Identifier", omniORB.typeCodeMapping["IDL:omg.org/CosTrading/Istring:1.0"]._d)
    _tc_Identifier = omniORB.tcInternal.createTypeCode(_ad_Identifier)
    omniORB.registerType(Identifier._NP_RepositoryId, _ad_Identifier, _tc_Identifier)
    
    # struct IncarnationNumber
    _0_CosTradingRepos.ServiceTypeRepository.IncarnationNumber = omniORB.newEmptyClass()
    class IncarnationNumber (omniORB.StructBase):
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/IncarnationNumber:1.0"

        _NP_ClassName = "CosTradingRepos.ServiceTypeRepository.IncarnationNumber"

        def __init__(self, high, low):
            self.high = high
            self.low = low
    
    _d_IncarnationNumber  = _0_CosTradingRepos.ServiceTypeRepository._d_IncarnationNumber = (omniORB.tcInternal.tv_struct, IncarnationNumber, IncarnationNumber._NP_RepositoryId, "IncarnationNumber", "high", omniORB.tcInternal.tv_ulong, "low", omniORB.tcInternal.tv_ulong)
    _tc_IncarnationNumber = omniORB.tcInternal.createTypeCode(_d_IncarnationNumber)
    omniORB.registerType(IncarnationNumber._NP_RepositoryId, _d_IncarnationNumber, _tc_IncarnationNumber)
    
    # struct TypeStruct
    _0_CosTradingRepos.ServiceTypeRepository.TypeStruct = omniORB.newEmptyClass()
    class TypeStruct (omniORB.StructBase):
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/TypeStruct:1.0"

        _NP_ClassName = "CosTradingRepos.ServiceTypeRepository.TypeStruct"

        def __init__(self, if_name, props, super_types, masked, incarnation):
            self.if_name = if_name
            self.props = props
            self.super_types = super_types
            self.masked = masked
            self.incarnation = incarnation
    
    _d_TypeStruct  = _0_CosTradingRepos.ServiceTypeRepository._d_TypeStruct = (omniORB.tcInternal.tv_struct, TypeStruct, TypeStruct._NP_RepositoryId, "TypeStruct", "if_name", omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/Identifier:1.0"], "props", omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/PropStructSeq:1.0"], "super_types", omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/ServiceTypeNameSeq:1.0"], "masked", omniORB.tcInternal.tv_boolean, "incarnation", omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/IncarnationNumber:1.0"])
    _tc_TypeStruct = omniORB.tcInternal.createTypeCode(_d_TypeStruct)
    omniORB.registerType(TypeStruct._NP_RepositoryId, _d_TypeStruct, _tc_TypeStruct)
    
    # enum ListOption
    all = omniORB.EnumItem("all", 0)
    since = omniORB.EnumItem("since", 1)
    ListOption = omniORB.Enum("IDL:omg.org/CosTradingRepos/ServiceTypeRepository/ListOption:1.0", (all, since,))

    _d_ListOption  = (omniORB.tcInternal.tv_enum, ListOption._NP_RepositoryId, "ListOption", ListOption._items)
    _tc_ListOption = omniORB.tcInternal.createTypeCode(_d_ListOption)
    omniORB.registerType(ListOption._NP_RepositoryId, _d_ListOption, _tc_ListOption)
    
    # union SpecifiedServiceTypes
    _0_CosTradingRepos.ServiceTypeRepository.SpecifiedServiceTypes = omniORB.newEmptyClass()
    class SpecifiedServiceTypes (omniORB.Union):
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/SpecifiedServiceTypes:1.0"
        _NP_ClassName = "CosTradingRepos.ServiceTypeRepository.SpecifiedServiceTypes"

    
    SpecifiedServiceTypes._m_to_d = {"incarnation": since}
    SpecifiedServiceTypes._d_to_m = {since: "incarnation"}
    SpecifiedServiceTypes._def_m  = None
    SpecifiedServiceTypes._def_d  = None

    _m_SpecifiedServiceTypes  = ((since, "incarnation", omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/IncarnationNumber:1.0"]),)
    _d_SpecifiedServiceTypes  = _0_CosTradingRepos.ServiceTypeRepository._d_SpecifiedServiceTypes = (omniORB.tcInternal.tv_union, SpecifiedServiceTypes, SpecifiedServiceTypes._NP_RepositoryId, "SpecifiedServiceTypes", omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/ListOption:1.0"], -1, _m_SpecifiedServiceTypes, None, {since: _m_SpecifiedServiceTypes[0]})
    _tc_SpecifiedServiceTypes = omniORB.tcInternal.createTypeCode(_d_SpecifiedServiceTypes)
    omniORB.registerType(SpecifiedServiceTypes._NP_RepositoryId, _d_SpecifiedServiceTypes, _tc_SpecifiedServiceTypes)
    
    # exception ServiceTypeExists
    _0_CosTradingRepos.ServiceTypeRepository.ServiceTypeExists = omniORB.newEmptyClass()
    class ServiceTypeExists (CORBA.UserException):
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/ServiceTypeExists:1.0"

        _NP_ClassName = "CosTradingRepos.ServiceTypeRepository.ServiceTypeExists"

        def __init__(self, name):
            CORBA.UserException.__init__(self, name)
            self.name = name
    
    _d_ServiceTypeExists  = (omniORB.tcInternal.tv_except, ServiceTypeExists, ServiceTypeExists._NP_RepositoryId, "ServiceTypeExists", "name", omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"])
    _tc_ServiceTypeExists = omniORB.tcInternal.createTypeCode(_d_ServiceTypeExists)
    omniORB.registerType(ServiceTypeExists._NP_RepositoryId, _d_ServiceTypeExists, _tc_ServiceTypeExists)
    
    # exception InterfaceTypeMismatch
    _0_CosTradingRepos.ServiceTypeRepository.InterfaceTypeMismatch = omniORB.newEmptyClass()
    class InterfaceTypeMismatch (CORBA.UserException):
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/InterfaceTypeMismatch:1.0"

        _NP_ClassName = "CosTradingRepos.ServiceTypeRepository.InterfaceTypeMismatch"

        def __init__(self, base_service, base_if, derived_service, derived_if):
            CORBA.UserException.__init__(self, base_service, base_if, derived_service, derived_if)
            self.base_service = base_service
            self.base_if = base_if
            self.derived_service = derived_service
            self.derived_if = derived_if
    
    _d_InterfaceTypeMismatch  = (omniORB.tcInternal.tv_except, InterfaceTypeMismatch, InterfaceTypeMismatch._NP_RepositoryId, "InterfaceTypeMismatch", "base_service", omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], "base_if", omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/Identifier:1.0"], "derived_service", omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], "derived_if", omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/Identifier:1.0"])
    _tc_InterfaceTypeMismatch = omniORB.tcInternal.createTypeCode(_d_InterfaceTypeMismatch)
    omniORB.registerType(InterfaceTypeMismatch._NP_RepositoryId, _d_InterfaceTypeMismatch, _tc_InterfaceTypeMismatch)
    
    # exception HasSubTypes
    _0_CosTradingRepos.ServiceTypeRepository.HasSubTypes = omniORB.newEmptyClass()
    class HasSubTypes (CORBA.UserException):
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/HasSubTypes:1.0"

        _NP_ClassName = "CosTradingRepos.ServiceTypeRepository.HasSubTypes"

        def __init__(self, the_type, sub_type):
            CORBA.UserException.__init__(self, the_type, sub_type)
            self.the_type = the_type
            self.sub_type = sub_type
    
    _d_HasSubTypes  = (omniORB.tcInternal.tv_except, HasSubTypes, HasSubTypes._NP_RepositoryId, "HasSubTypes", "the_type", omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], "sub_type", omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"])
    _tc_HasSubTypes = omniORB.tcInternal.createTypeCode(_d_HasSubTypes)
    omniORB.registerType(HasSubTypes._NP_RepositoryId, _d_HasSubTypes, _tc_HasSubTypes)
    
    # exception AlreadyMasked
    _0_CosTradingRepos.ServiceTypeRepository.AlreadyMasked = omniORB.newEmptyClass()
    class AlreadyMasked (CORBA.UserException):
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/AlreadyMasked:1.0"

        _NP_ClassName = "CosTradingRepos.ServiceTypeRepository.AlreadyMasked"

        def __init__(self, name):
            CORBA.UserException.__init__(self, name)
            self.name = name
    
    _d_AlreadyMasked  = (omniORB.tcInternal.tv_except, AlreadyMasked, AlreadyMasked._NP_RepositoryId, "AlreadyMasked", "name", omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"])
    _tc_AlreadyMasked = omniORB.tcInternal.createTypeCode(_d_AlreadyMasked)
    omniORB.registerType(AlreadyMasked._NP_RepositoryId, _d_AlreadyMasked, _tc_AlreadyMasked)
    
    # exception NotMasked
    _0_CosTradingRepos.ServiceTypeRepository.NotMasked = omniORB.newEmptyClass()
    class NotMasked (CORBA.UserException):
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/NotMasked:1.0"

        _NP_ClassName = "CosTradingRepos.ServiceTypeRepository.NotMasked"

        def __init__(self, name):
            CORBA.UserException.__init__(self, name)
            self.name = name
    
    _d_NotMasked  = (omniORB.tcInternal.tv_except, NotMasked, NotMasked._NP_RepositoryId, "NotMasked", "name", omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"])
    _tc_NotMasked = omniORB.tcInternal.createTypeCode(_d_NotMasked)
    omniORB.registerType(NotMasked._NP_RepositoryId, _d_NotMasked, _tc_NotMasked)
    
    # exception ValueTypeRedefinition
    _0_CosTradingRepos.ServiceTypeRepository.ValueTypeRedefinition = omniORB.newEmptyClass()
    class ValueTypeRedefinition (CORBA.UserException):
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/ValueTypeRedefinition:1.0"

        _NP_ClassName = "CosTradingRepos.ServiceTypeRepository.ValueTypeRedefinition"

        def __init__(self, type_1, definition_1, type_2, definition_2):
            CORBA.UserException.__init__(self, type_1, definition_1, type_2, definition_2)
            self.type_1 = type_1
            self.definition_1 = definition_1
            self.type_2 = type_2
            self.definition_2 = definition_2
    
    _d_ValueTypeRedefinition  = (omniORB.tcInternal.tv_except, ValueTypeRedefinition, ValueTypeRedefinition._NP_RepositoryId, "ValueTypeRedefinition", "type_1", omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], "definition_1", omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/PropStruct:1.0"], "type_2", omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], "definition_2", omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/PropStruct:1.0"])
    _tc_ValueTypeRedefinition = omniORB.tcInternal.createTypeCode(_d_ValueTypeRedefinition)
    omniORB.registerType(ValueTypeRedefinition._NP_RepositoryId, _d_ValueTypeRedefinition, _tc_ValueTypeRedefinition)
    
    # exception DuplicateServiceTypeName
    _0_CosTradingRepos.ServiceTypeRepository.DuplicateServiceTypeName = omniORB.newEmptyClass()
    class DuplicateServiceTypeName (CORBA.UserException):
        _NP_RepositoryId = "IDL:omg.org/CosTradingRepos/ServiceTypeRepository/DuplicateServiceTypeName:1.0"

        _NP_ClassName = "CosTradingRepos.ServiceTypeRepository.DuplicateServiceTypeName"

        def __init__(self, name):
            CORBA.UserException.__init__(self, name)
            self.name = name
    
    _d_DuplicateServiceTypeName  = (omniORB.tcInternal.tv_except, DuplicateServiceTypeName, DuplicateServiceTypeName._NP_RepositoryId, "DuplicateServiceTypeName", "name", omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"])
    _tc_DuplicateServiceTypeName = omniORB.tcInternal.createTypeCode(_d_DuplicateServiceTypeName)
    omniORB.registerType(DuplicateServiceTypeName._NP_RepositoryId, _d_DuplicateServiceTypeName, _tc_DuplicateServiceTypeName)


_0_CosTradingRepos.ServiceTypeRepository = ServiceTypeRepository
_0_CosTradingRepos._tc_ServiceTypeRepository = omniORB.tcInternal.createTypeCode(_0_CosTradingRepos._d_ServiceTypeRepository)
omniORB.registerType(ServiceTypeRepository._NP_RepositoryId, _0_CosTradingRepos._d_ServiceTypeRepository, _0_CosTradingRepos._tc_ServiceTypeRepository)

# ServiceTypeRepository operations and attributes
ServiceTypeRepository._d__get_incarnation = ((),(omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/IncarnationNumber:1.0"],),None)
ServiceTypeRepository._d_add_type = ((omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/Identifier:1.0"], omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/PropStructSeq:1.0"], omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/ServiceTypeNameSeq:1.0"]), (omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/IncarnationNumber:1.0"], ), {_0_CosTrading.IllegalServiceType._NP_RepositoryId: _0_CosTrading._d_IllegalServiceType, _0_CosTradingRepos.ServiceTypeRepository.ServiceTypeExists._NP_RepositoryId: _0_CosTradingRepos.ServiceTypeRepository._d_ServiceTypeExists, _0_CosTradingRepos.ServiceTypeRepository.InterfaceTypeMismatch._NP_RepositoryId: _0_CosTradingRepos.ServiceTypeRepository._d_InterfaceTypeMismatch, _0_CosTrading.IllegalPropertyName._NP_RepositoryId: _0_CosTrading._d_IllegalPropertyName, _0_CosTrading.DuplicatePropertyName._NP_RepositoryId: _0_CosTrading._d_DuplicatePropertyName, _0_CosTradingRepos.ServiceTypeRepository.ValueTypeRedefinition._NP_RepositoryId: _0_CosTradingRepos.ServiceTypeRepository._d_ValueTypeRedefinition, _0_CosTrading.UnknownServiceType._NP_RepositoryId: _0_CosTrading._d_UnknownServiceType, _0_CosTradingRepos.ServiceTypeRepository.DuplicateServiceTypeName._NP_RepositoryId: _0_CosTradingRepos.ServiceTypeRepository._d_DuplicateServiceTypeName})
ServiceTypeRepository._d_remove_type = ((omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], ), (), {_0_CosTrading.IllegalServiceType._NP_RepositoryId: _0_CosTrading._d_IllegalServiceType, _0_CosTrading.UnknownServiceType._NP_RepositoryId: _0_CosTrading._d_UnknownServiceType, _0_CosTradingRepos.ServiceTypeRepository.HasSubTypes._NP_RepositoryId: _0_CosTradingRepos.ServiceTypeRepository._d_HasSubTypes})
ServiceTypeRepository._d_list_types = ((omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/SpecifiedServiceTypes:1.0"], ), (omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/ServiceTypeNameSeq:1.0"], ), None)
ServiceTypeRepository._d_describe_type = ((omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], ), (omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/TypeStruct:1.0"], ), {_0_CosTrading.IllegalServiceType._NP_RepositoryId: _0_CosTrading._d_IllegalServiceType, _0_CosTrading.UnknownServiceType._NP_RepositoryId: _0_CosTrading._d_UnknownServiceType})
ServiceTypeRepository._d_fully_describe_type = ((omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], ), (omniORB.typeMapping["IDL:omg.org/CosTradingRepos/ServiceTypeRepository/TypeStruct:1.0"], ), {_0_CosTrading.IllegalServiceType._NP_RepositoryId: _0_CosTrading._d_IllegalServiceType, _0_CosTrading.UnknownServiceType._NP_RepositoryId: _0_CosTrading._d_UnknownServiceType})
ServiceTypeRepository._d_mask_type = ((omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], ), (), {_0_CosTrading.IllegalServiceType._NP_RepositoryId: _0_CosTrading._d_IllegalServiceType, _0_CosTrading.UnknownServiceType._NP_RepositoryId: _0_CosTrading._d_UnknownServiceType, _0_CosTradingRepos.ServiceTypeRepository.AlreadyMasked._NP_RepositoryId: _0_CosTradingRepos.ServiceTypeRepository._d_AlreadyMasked})
ServiceTypeRepository._d_unmask_type = ((omniORB.typeMapping["IDL:omg.org/CosTrading/ServiceTypeName:1.0"], ), (), {_0_CosTrading.IllegalServiceType._NP_RepositoryId: _0_CosTrading._d_IllegalServiceType, _0_CosTrading.UnknownServiceType._NP_RepositoryId: _0_CosTrading._d_UnknownServiceType, _0_CosTradingRepos.ServiceTypeRepository.NotMasked._NP_RepositoryId: _0_CosTradingRepos.ServiceTypeRepository._d_NotMasked})

# ServiceTypeRepository object reference
class _objref_ServiceTypeRepository (CORBA.Object):
    _NP_RepositoryId = ServiceTypeRepository._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def _get_incarnation(self, *args):
        return _omnipy.invoke(self, "_get_incarnation", _0_CosTradingRepos.ServiceTypeRepository._d__get_incarnation, args)

    def add_type(self, *args):
        return _omnipy.invoke(self, "add_type", _0_CosTradingRepos.ServiceTypeRepository._d_add_type, args)

    def remove_type(self, *args):
        return _omnipy.invoke(self, "remove_type", _0_CosTradingRepos.ServiceTypeRepository._d_remove_type, args)

    def list_types(self, *args):
        return _omnipy.invoke(self, "list_types", _0_CosTradingRepos.ServiceTypeRepository._d_list_types, args)

    def describe_type(self, *args):
        return _omnipy.invoke(self, "describe_type", _0_CosTradingRepos.ServiceTypeRepository._d_describe_type, args)

    def fully_describe_type(self, *args):
        return _omnipy.invoke(self, "fully_describe_type", _0_CosTradingRepos.ServiceTypeRepository._d_fully_describe_type, args)

    def mask_type(self, *args):
        return _omnipy.invoke(self, "mask_type", _0_CosTradingRepos.ServiceTypeRepository._d_mask_type, args)

    def unmask_type(self, *args):
        return _omnipy.invoke(self, "unmask_type", _0_CosTradingRepos.ServiceTypeRepository._d_unmask_type, args)

    __methods__ = ["_get_incarnation", "add_type", "remove_type", "list_types", "describe_type", "fully_describe_type", "mask_type", "unmask_type"] + CORBA.Object.__methods__

omniORB.registerObjref(ServiceTypeRepository._NP_RepositoryId, _objref_ServiceTypeRepository)
_0_CosTradingRepos._objref_ServiceTypeRepository = _objref_ServiceTypeRepository
del ServiceTypeRepository, _objref_ServiceTypeRepository

# ServiceTypeRepository skeleton
__name__ = "CosTradingRepos__POA"
class ServiceTypeRepository (PortableServer.Servant):
    _NP_RepositoryId = _0_CosTradingRepos.ServiceTypeRepository._NP_RepositoryId


    _omni_op_d = {"_get_incarnation": _0_CosTradingRepos.ServiceTypeRepository._d__get_incarnation, "add_type": _0_CosTradingRepos.ServiceTypeRepository._d_add_type, "remove_type": _0_CosTradingRepos.ServiceTypeRepository._d_remove_type, "list_types": _0_CosTradingRepos.ServiceTypeRepository._d_list_types, "describe_type": _0_CosTradingRepos.ServiceTypeRepository._d_describe_type, "fully_describe_type": _0_CosTradingRepos.ServiceTypeRepository._d_fully_describe_type, "mask_type": _0_CosTradingRepos.ServiceTypeRepository._d_mask_type, "unmask_type": _0_CosTradingRepos.ServiceTypeRepository._d_unmask_type}

ServiceTypeRepository._omni_skeleton = ServiceTypeRepository
_0_CosTradingRepos__POA.ServiceTypeRepository = ServiceTypeRepository
omniORB.registerSkeleton(ServiceTypeRepository._NP_RepositoryId, ServiceTypeRepository)
del ServiceTypeRepository
__name__ = "CosTradingRepos"

#
# End of module "CosTradingRepos"
#
__name__ = "CosTradingRepos_idl"

_exported_modules = ( "CosTradingRepos", )

# The end.
