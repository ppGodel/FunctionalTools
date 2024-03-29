#!/usr/bin/env python3
from context import functor
from unittest import TestCase


class FunctorTest(TestCase):
    def test_identity(self):
        def identity(x):
            return x
        value = 'hola'
        functor_identity = functor(identity)
        return_value = functor_identity(value)
        self.assertEqual(value, return_value)

    def test_composition(self):
        def fn_f(x):
            return x ** 3

        def fn_g(x):
            return x + 10

        def gof(x):
            return fn_g(fn_f(x))

        value = 7
        composited = functor(fn_f).map(fn_g)
        self.assertEqual(composited(value), gof(value))


# functor_1 = functor(add3)  # type Functor[int]
# functor_post = functor_1.map(multiply5).map(to_string)
# print(functor_post(4.0))
# functor_2 = functor.of(4.0)
# functor_pre = functor_2.map(add3).map(multiply5).map(to_string)
# print(functor_pre())
# print(f'combined1: {functor_post(functor_2())}')
# functor_3 = functor.of('Hola')  # type Functor[str]
# functor_pre_str = functor_3.map(len).map(add3).map(multiply5).map(to_string)
# print(functor_pre_str())
# # side efect horrible que obtiene un diccionario del mundo real
# functor_dict = functor.of({'name': 'Jose'})
#
# functor_get_name = functor(lambda dic: dic.get('name', 'NoName')).\
#     map(str.upper).map(lambda x: f'my name is {x}')  # pure function
# name_val = functor_get_name(functor_dict())


# def side_effect_save(x: Any) -> None:
#     print(f'printed: {x}')
#
#
# functor_print = functor(side_effect_save)
# functor_print.combine(functor_get_name.combine(functor.of({})))()
# functor_print.combine(functor_get_name).combine(functor.of({}))()
# # backwards first the final side effect and xform are combined
# # finally the inital side effect is combined and then executed
# functor_print.combine(functor_get_name).combine(functor_dict)()
# # forward, the initial side effect is maped to the xform and then
# # mapped to the finall side effect, then it is executed
# functor_dict.map(functor_get_name).map(functor_print)()
