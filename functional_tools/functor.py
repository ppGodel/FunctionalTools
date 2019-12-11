#!/usr/bin/env python3
from typing import Dict, Callable, Any, TypeVar, _alias

T = TypeVar('T')

# example of functor as function but a class seems better for python
def _functor_from_function(f: Callable[[Any], Any]) -> Callable[[Any],Any]:
    def map(g: Callable[[Any], Any]) -> Callable[[Any],Any]:
        def fog(x: Any)-> Any:
            return g(f(x))
        return functor(fog)
    def effect(x):
        return f(x)

    return {'map': map, 'effect': effect}


class functor(object):
    def __init__(self, f: Callable):
        self.f = f

    def map(self, g: Callable) -> 'functor':
        def fog(x: Any) -> Any:
            return g(self.f(x))
        return functor(fog)

    def __call__(self, x: Any = None) -> Any:
        return self.f(x)

    def combine(self, _functor: 'functor', x: Any = None) -> 'Functor':
        return _functor.map(self.f)

    @classmethod
    def of(cls, x: Any) -> 'functor':
        def f(_: Any) -> Any:
            return x
        return functor(f)

Functor = _alias(functor, T, inst=False)
