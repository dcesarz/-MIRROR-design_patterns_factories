import cProfile

# noinspection PyUnresolvedReferences
import implementation_tests

print("\n========================REGISTRATION========================\n")
cProfile.runctx('implementation_tests.register()', globals(), locals())
print("\n========================REGISTRATION_WITH_REFLECTION========================\n")
cProfile.runctx('implementation_tests.register_with_reflection()', globals(), locals())
print("\n========================ABSTRACT_FACTORY========================\n")
cProfile.runctx('implementation_tests.exec_abstract(10000)', globals(), locals())
print("\n========================FACTORY_METHOD========================\n")
cProfile.runctx('implementation_tests.exec_fm(10000)', globals(), locals())
print("\n========================SIMPLE_FACTORY========================\n")
cProfile.runctx('implementation_tests.exec_simple(10000)', globals(), locals())
print("\n========================FACTORY_REGISTRATION========================\n")
cProfile.runctx('implementation_tests.exec_fr(10000)', globals(), locals())
print("\n========================FACTORY_REGISTRATION_WITH_REFLECTION========================\n")
cProfile.runctx('implementation_tests.exec_frr(10000)', globals(), locals())
