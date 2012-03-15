# Python stubs generated by omniidl from ..\..\..\..\..\idl\COS\LifeCycleService.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)

# #include "CosNaming.idl"
import CosNaming_idl
_0_CosNaming = omniORB.openModule("CosNaming")
_0_CosNaming__POA = omniORB.openModule("CosNaming__POA")
# #include "CosLifeCycle.idl"
import CosLifeCycle_idl
_0_CosLifeCycle = omniORB.openModule("CosLifeCycle")
_0_CosLifeCycle__POA = omniORB.openModule("CosLifeCycle__POA")

#
# Start of module "LifeCycleService"
#
__name__ = "LifeCycleService"
_0_LifeCycleService = omniORB.openModule("LifeCycleService", r"..\..\..\..\..\idl\COS\LifeCycleService.idl")
_0_LifeCycleService__POA = omniORB.openModule("LifeCycleService__POA", r"..\..\..\..\..\idl\COS\LifeCycleService.idl")


# typedef ... PolicyList
class PolicyList:
    _NP_RepositoryId = "IDL:omg.org/LifeCycleService/PolicyList:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_LifeCycleService.PolicyList = PolicyList
_0_LifeCycleService._d_PolicyList  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosLifeCycle/NameValuePair:1.0"], 0)
_0_LifeCycleService._ad_PolicyList = (omniORB.tcInternal.tv_alias, PolicyList._NP_RepositoryId, "PolicyList", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosLifeCycle/NameValuePair:1.0"], 0))
_0_LifeCycleService._tc_PolicyList = omniORB.tcInternal.createTypeCode(_0_LifeCycleService._ad_PolicyList)
omniORB.registerType(PolicyList._NP_RepositoryId, _0_LifeCycleService._ad_PolicyList, _0_LifeCycleService._tc_PolicyList)
del PolicyList

# typedef ... Keys
class Keys:
    _NP_RepositoryId = "IDL:omg.org/LifeCycleService/Keys:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_LifeCycleService.Keys = Keys
_0_LifeCycleService._d_Keys  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Key:1.0"], 0)
_0_LifeCycleService._ad_Keys = (omniORB.tcInternal.tv_alias, Keys._NP_RepositoryId, "Keys", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Key:1.0"], 0))
_0_LifeCycleService._tc_Keys = omniORB.tcInternal.createTypeCode(_0_LifeCycleService._ad_Keys)
omniORB.registerType(Keys._NP_RepositoryId, _0_LifeCycleService._ad_Keys, _0_LifeCycleService._tc_Keys)
del Keys

# typedef ... PropertyList
class PropertyList:
    _NP_RepositoryId = "IDL:omg.org/LifeCycleService/PropertyList:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_LifeCycleService.PropertyList = PropertyList
_0_LifeCycleService._d_PropertyList  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosLifeCycle/NameValuePair:1.0"], 0)
_0_LifeCycleService._ad_PropertyList = (omniORB.tcInternal.tv_alias, PropertyList._NP_RepositoryId, "PropertyList", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosLifeCycle/NameValuePair:1.0"], 0))
_0_LifeCycleService._tc_PropertyList = omniORB.tcInternal.createTypeCode(_0_LifeCycleService._ad_PropertyList)
omniORB.registerType(PropertyList._NP_RepositoryId, _0_LifeCycleService._ad_PropertyList, _0_LifeCycleService._tc_PropertyList)
del PropertyList

# typedef ... NameComponents
class NameComponents:
    _NP_RepositoryId = "IDL:omg.org/LifeCycleService/NameComponents:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_LifeCycleService.NameComponents = NameComponents
_0_LifeCycleService._d_NameComponents  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosNaming/NameComponent:1.0"], 0)
_0_LifeCycleService._ad_NameComponents = (omniORB.tcInternal.tv_alias, NameComponents._NP_RepositoryId, "NameComponents", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosNaming/NameComponent:1.0"], 0))
_0_LifeCycleService._tc_NameComponents = omniORB.tcInternal.createTypeCode(_0_LifeCycleService._ad_NameComponents)
omniORB.registerType(NameComponents._NP_RepositoryId, _0_LifeCycleService._ad_NameComponents, _0_LifeCycleService._tc_NameComponents)
del NameComponents

# interface LifeCycleServiceAdmin
_0_LifeCycleService._d_LifeCycleServiceAdmin = (omniORB.tcInternal.tv_objref, "IDL:omg.org/LifeCycleService/LifeCycleServiceAdmin:1.0", "LifeCycleServiceAdmin")
omniORB.typeMapping["IDL:omg.org/LifeCycleService/LifeCycleServiceAdmin:1.0"] = _0_LifeCycleService._d_LifeCycleServiceAdmin
_0_LifeCycleService.LifeCycleServiceAdmin = omniORB.newEmptyClass()
class LifeCycleServiceAdmin :
    _NP_RepositoryId = _0_LifeCycleService._d_LifeCycleServiceAdmin[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_LifeCycleService.LifeCycleServiceAdmin = LifeCycleServiceAdmin
_0_LifeCycleService._tc_LifeCycleServiceAdmin = omniORB.tcInternal.createTypeCode(_0_LifeCycleService._d_LifeCycleServiceAdmin)
omniORB.registerType(LifeCycleServiceAdmin._NP_RepositoryId, _0_LifeCycleService._d_LifeCycleServiceAdmin, _0_LifeCycleService._tc_LifeCycleServiceAdmin)

# LifeCycleServiceAdmin operations and attributes
LifeCycleServiceAdmin._d__get_policies = ((),(omniORB.typeMapping["IDL:omg.org/LifeCycleService/PolicyList:1.0"],),None)
LifeCycleServiceAdmin._d__set_policies = ((omniORB.typeMapping["IDL:omg.org/LifeCycleService/PolicyList:1.0"],),(),None)
LifeCycleServiceAdmin._d_bind_generic_factory = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/GenericFactory:1.0"], omniORB.typeMapping["IDL:omg.org/CosNaming/NameComponent:1.0"], omniORB.typeMapping["IDL:omg.org/LifeCycleService/Keys:1.0"], omniORB.typeMapping["IDL:omg.org/LifeCycleService/PropertyList:1.0"]), (), {_0_CosNaming.NamingContext.AlreadyBound._NP_RepositoryId: _0_CosNaming.NamingContext._d_AlreadyBound, _0_CosNaming.NamingContext.InvalidName._NP_RepositoryId: _0_CosNaming.NamingContext._d_InvalidName})
LifeCycleServiceAdmin._d_unbind_generic_factory = ((omniORB.typeMapping["IDL:omg.org/CosNaming/NameComponent:1.0"], ), (), {_0_CosNaming.NamingContext.NotFound._NP_RepositoryId: _0_CosNaming.NamingContext._d_NotFound, _0_CosNaming.NamingContext.InvalidName._NP_RepositoryId: _0_CosNaming.NamingContext._d_InvalidName})
LifeCycleServiceAdmin._d_resolve_generic_factory = ((omniORB.typeMapping["IDL:omg.org/CosNaming/NameComponent:1.0"], ), (omniORB.typeMapping["IDL:omg.org/CosLifeCycle/GenericFactory:1.0"], ), {_0_CosNaming.NamingContext.NotFound._NP_RepositoryId: _0_CosNaming.NamingContext._d_NotFound, _0_CosNaming.NamingContext.InvalidName._NP_RepositoryId: _0_CosNaming.NamingContext._d_InvalidName})
LifeCycleServiceAdmin._d_list_generic_factories = ((), (omniORB.typeMapping["IDL:omg.org/LifeCycleService/NameComponents:1.0"], ), None)
LifeCycleServiceAdmin._d_match_service = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/GenericFactory:1.0"], ), (omniORB.tcInternal.tv_boolean, ), None)
LifeCycleServiceAdmin._d_get_hint = ((), ((omniORB.tcInternal.tv_string,0), ), None)
LifeCycleServiceAdmin._d_get_link_properties = ((omniORB.typeMapping["IDL:omg.org/CosNaming/NameComponent:1.0"], ), (omniORB.typeMapping["IDL:omg.org/LifeCycleService/Keys:1.0"], omniORB.typeMapping["IDL:omg.org/LifeCycleService/PropertyList:1.0"]), {_0_CosNaming.NamingContext.NotFound._NP_RepositoryId: _0_CosNaming.NamingContext._d_NotFound, _0_CosNaming.NamingContext.InvalidName._NP_RepositoryId: _0_CosNaming.NamingContext._d_InvalidName})

# LifeCycleServiceAdmin object reference
class _objref_LifeCycleServiceAdmin (CORBA.Object):
    _NP_RepositoryId = LifeCycleServiceAdmin._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def _get_policies(self, *args):
        return _omnipy.invoke(self, "_get_policies", _0_LifeCycleService.LifeCycleServiceAdmin._d__get_policies, args)

    def _set_policies(self, *args):
        return _omnipy.invoke(self, "_set_policies", _0_LifeCycleService.LifeCycleServiceAdmin._d__set_policies, args)

    def bind_generic_factory(self, *args):
        return _omnipy.invoke(self, "bind_generic_factory", _0_LifeCycleService.LifeCycleServiceAdmin._d_bind_generic_factory, args)

    def unbind_generic_factory(self, *args):
        return _omnipy.invoke(self, "unbind_generic_factory", _0_LifeCycleService.LifeCycleServiceAdmin._d_unbind_generic_factory, args)

    def resolve_generic_factory(self, *args):
        return _omnipy.invoke(self, "resolve_generic_factory", _0_LifeCycleService.LifeCycleServiceAdmin._d_resolve_generic_factory, args)

    def list_generic_factories(self, *args):
        return _omnipy.invoke(self, "list_generic_factories", _0_LifeCycleService.LifeCycleServiceAdmin._d_list_generic_factories, args)

    def match_service(self, *args):
        return _omnipy.invoke(self, "match_service", _0_LifeCycleService.LifeCycleServiceAdmin._d_match_service, args)

    def get_hint(self, *args):
        return _omnipy.invoke(self, "get_hint", _0_LifeCycleService.LifeCycleServiceAdmin._d_get_hint, args)

    def get_link_properties(self, *args):
        return _omnipy.invoke(self, "get_link_properties", _0_LifeCycleService.LifeCycleServiceAdmin._d_get_link_properties, args)

    __methods__ = ["_get_policies", "_set_policies", "bind_generic_factory", "unbind_generic_factory", "resolve_generic_factory", "list_generic_factories", "match_service", "get_hint", "get_link_properties"] + CORBA.Object.__methods__

omniORB.registerObjref(LifeCycleServiceAdmin._NP_RepositoryId, _objref_LifeCycleServiceAdmin)
_0_LifeCycleService._objref_LifeCycleServiceAdmin = _objref_LifeCycleServiceAdmin
del LifeCycleServiceAdmin, _objref_LifeCycleServiceAdmin

# LifeCycleServiceAdmin skeleton
__name__ = "LifeCycleService__POA"
class LifeCycleServiceAdmin (PortableServer.Servant):
    _NP_RepositoryId = _0_LifeCycleService.LifeCycleServiceAdmin._NP_RepositoryId


    _omni_op_d = {"_get_policies": _0_LifeCycleService.LifeCycleServiceAdmin._d__get_policies, "_set_policies": _0_LifeCycleService.LifeCycleServiceAdmin._d__set_policies, "bind_generic_factory": _0_LifeCycleService.LifeCycleServiceAdmin._d_bind_generic_factory, "unbind_generic_factory": _0_LifeCycleService.LifeCycleServiceAdmin._d_unbind_generic_factory, "resolve_generic_factory": _0_LifeCycleService.LifeCycleServiceAdmin._d_resolve_generic_factory, "list_generic_factories": _0_LifeCycleService.LifeCycleServiceAdmin._d_list_generic_factories, "match_service": _0_LifeCycleService.LifeCycleServiceAdmin._d_match_service, "get_hint": _0_LifeCycleService.LifeCycleServiceAdmin._d_get_hint, "get_link_properties": _0_LifeCycleService.LifeCycleServiceAdmin._d_get_link_properties}

LifeCycleServiceAdmin._omni_skeleton = LifeCycleServiceAdmin
_0_LifeCycleService__POA.LifeCycleServiceAdmin = LifeCycleServiceAdmin
omniORB.registerSkeleton(LifeCycleServiceAdmin._NP_RepositoryId, LifeCycleServiceAdmin)
del LifeCycleServiceAdmin
__name__ = "LifeCycleService"

#
# End of module "LifeCycleService"
#
__name__ = "LifeCycleService_idl"

_exported_modules = ( "LifeCycleService", )

# The end.
