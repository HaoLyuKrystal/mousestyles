from mousestyles.GLRT_distribution import (random_powerlaw, random_exp,
                                           hypo_powerLaw_null, hypo_exp_null)
import numpy
import math


def test_random_powerlaw():
    assert type(random_powerlaw(4, 2)) is numpy.ndarray


def test_random_exp():
    assert type(random_exp(4, 2)) is numpy.ndarray


def test_hypo_powerLaw_null():
    assert abs(hypo_powerLaw_null(0, 0, 0) - 0.007) <= 1.96 * \
        math.sqrt(0.007 * 0.993)


def test_hypo_exp_null():
    assert abs(hypo_exp_null(0, 0, 0) - 1.0) <= 1.96 * math.sqrt(0.005 * 0.995)
