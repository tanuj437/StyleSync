# Modified by Tanuj Saxena
# Copyright (c) Facebook, Inc. and its affiliates.

from . import DensePoseChartConfidencePredictorMixin, DensePoseChartPredictor
from .registry import DENSEPOSE_PREDICTOR_REGISTRY


@DENSEPOSE_PREDICTOR_REGISTRY.register()
class DensePoseChartWithConfidencePredictor(
    DensePoseChartConfidencePredictorMixin, DensePoseChartPredictor
):
    """
    Predictor that combines chart and chart confidence estimation
    """

    pass
