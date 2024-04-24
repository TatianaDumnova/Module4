# В этом модуле вызываю все функции из трех других модулей
# пакета PackageMath разными способами

from Module1 import function1, function2, function3, function4

function1()
function2()
function3()
function4()

from Module2 import *

function1()
function2()
function3()
function4()

import Module3 as m

m.function1()
m.function2()
m.function3()
