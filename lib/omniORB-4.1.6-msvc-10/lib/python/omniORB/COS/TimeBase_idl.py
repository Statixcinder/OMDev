# Python stubs generated by omniidl from ..\..\..\..\..\idl\COS\TimeBase.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "TimeBase"
#
__name__ = "TimeBase"
_0_TimeBase = omniORB.openModule("TimeBase", r"..\..\..\..\..\idl\COS\TimeBase.idl")
_0_TimeBase__POA = omniORB.openModule("TimeBase__POA", r"..\..\..\..\..\idl\COS\TimeBase.idl")


# typedef ... TimeT
class TimeT:
    _NP_RepositoryId = "IDL:omg.org/TimeBase/TimeT:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_TimeBase.TimeT = TimeT
_0_TimeBase._d_TimeT  = omniORB.tcInternal.tv_ulonglong
_0_TimeBase._ad_TimeT = (omniORB.tcInternal.tv_alias, TimeT._NP_RepositoryId, "TimeT", omniORB.tcInternal.tv_ulonglong)
_0_TimeBase._tc_TimeT = omniORB.tcInternal.createTypeCode(_0_TimeBase._ad_TimeT)
omniORB.registerType(TimeT._NP_RepositoryId, _0_TimeBase._ad_TimeT, _0_TimeBase._tc_TimeT)
del TimeT

# typedef ... InaccuracyT
class InaccuracyT:
    _NP_RepositoryId = "IDL:omg.org/TimeBase/InaccuracyT:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_TimeBase.InaccuracyT = InaccuracyT
_0_TimeBase._d_InaccuracyT  = omniORB.typeMapping["IDL:omg.org/TimeBase/TimeT:1.0"]
_0_TimeBase._ad_InaccuracyT = (omniORB.tcInternal.tv_alias, InaccuracyT._NP_RepositoryId, "InaccuracyT", omniORB.typeCodeMapping["IDL:omg.org/TimeBase/TimeT:1.0"]._d)
_0_TimeBase._tc_InaccuracyT = omniORB.tcInternal.createTypeCode(_0_TimeBase._ad_InaccuracyT)
omniORB.registerType(InaccuracyT._NP_RepositoryId, _0_TimeBase._ad_InaccuracyT, _0_TimeBase._tc_InaccuracyT)
del InaccuracyT

# typedef ... TdfT
class TdfT:
    _NP_RepositoryId = "IDL:omg.org/TimeBase/TdfT:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_TimeBase.TdfT = TdfT
_0_TimeBase._d_TdfT  = omniORB.tcInternal.tv_short
_0_TimeBase._ad_TdfT = (omniORB.tcInternal.tv_alias, TdfT._NP_RepositoryId, "TdfT", omniORB.tcInternal.tv_short)
_0_TimeBase._tc_TdfT = omniORB.tcInternal.createTypeCode(_0_TimeBase._ad_TdfT)
omniORB.registerType(TdfT._NP_RepositoryId, _0_TimeBase._ad_TdfT, _0_TimeBase._tc_TdfT)
del TdfT

# struct UtcT
_0_TimeBase.UtcT = omniORB.newEmptyClass()
class UtcT (omniORB.StructBase):
    _NP_RepositoryId = "IDL:omg.org/TimeBase/UtcT:1.0"

    def __init__(self, time, inacclo, inacchi, tdf):
        self.time = time
        self.inacclo = inacclo
        self.inacchi = inacchi
        self.tdf = tdf

_0_TimeBase.UtcT = UtcT
_0_TimeBase._d_UtcT  = (omniORB.tcInternal.tv_struct, UtcT, UtcT._NP_RepositoryId, "UtcT", "time", omniORB.typeMapping["IDL:omg.org/TimeBase/TimeT:1.0"], "inacclo", omniORB.tcInternal.tv_ulong, "inacchi", omniORB.tcInternal.tv_ushort, "tdf", omniORB.typeMapping["IDL:omg.org/TimeBase/TdfT:1.0"])
_0_TimeBase._tc_UtcT = omniORB.tcInternal.createTypeCode(_0_TimeBase._d_UtcT)
omniORB.registerType(UtcT._NP_RepositoryId, _0_TimeBase._d_UtcT, _0_TimeBase._tc_UtcT)
del UtcT

# struct IntervalT
_0_TimeBase.IntervalT = omniORB.newEmptyClass()
class IntervalT (omniORB.StructBase):
    _NP_RepositoryId = "IDL:omg.org/TimeBase/IntervalT:1.0"

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

_0_TimeBase.IntervalT = IntervalT
_0_TimeBase._d_IntervalT  = (omniORB.tcInternal.tv_struct, IntervalT, IntervalT._NP_RepositoryId, "IntervalT", "lower_bound", omniORB.typeMapping["IDL:omg.org/TimeBase/TimeT:1.0"], "upper_bound", omniORB.typeMapping["IDL:omg.org/TimeBase/TimeT:1.0"])
_0_TimeBase._tc_IntervalT = omniORB.tcInternal.createTypeCode(_0_TimeBase._d_IntervalT)
omniORB.registerType(IntervalT._NP_RepositoryId, _0_TimeBase._d_IntervalT, _0_TimeBase._tc_IntervalT)
del IntervalT

#
# End of module "TimeBase"
#
__name__ = "TimeBase_idl"

_exported_modules = ( "TimeBase", )

# The end.
