"""
This is a performance-oriented scoring engine for ONNX (Open Neural Network Exchange) models.
See `aka.ms/onnxruntime <https://aka.ms/onnxruntime/>`_
or its project on `Github <https://github.com/microsoft/onnxruntime/>`_.
"""

import contextlib

__version__ = "1.29.0"
__author__ = "Microsoft"

# Perform device version validation (e.g. check Cuda version for onnxruntime-training package)
#   so that we can determine whether to import onnxruntime.training.ortmodule first
# for the onnxruntime package
# Before importing onnxruntime.training.ortmodule onnxruntime.capi._pybind_state is needed
# But if a required Cuda version isn't found then the _pybind_state would have already raised an exception
# So we need to capture the exception and persist in performing Cuda version validation to
#   communicate meaningful messages to the user
# Device version validation comes before the raising of the saved exception
try:
    from onnxruntime.capi._pybind_state import (
        ExecutionMode,  # noqa: F401
        ExecutionOrder,  # noqa: F401
        GraphOptimizationLevel,  # noqa: F401
        LoraAdapter,  # noqa: F401
        ModelMetadata,  # noqa: F401
        NodeArg,  # noqa: F401
        OrtAllocatorType,  # noqa: F401
        OrtArenaCfg,  # noqa: F401
        OrtCompileApiFlags,  # noqa: F401
        OrtDeviceMemoryType,  # noqa: F401
        OrtEpAssignedNode,  # noqa: F401
        OrtEpAssignedSubgraph,  # noqa: F401
        OrtEpDevice,  # noqa: F401
        OrtExecutionProviderDevicePolicy,  # noqa: F401
        OrtExternalInitializerInfo,  # noqa: F401
        OrtHardwareDevice,  # noqa: F401
        OrtHardwareDeviceType,  # noqa: F401
        OrtMemoryInfo,  # noqa: F401
        OrtMemoryInfoDeviceType,  # noqa: F401
        OrtMemType,  # noqa: F401
        OrtSparseFormat,  # noqa: F401
        OrtSyncStream,  # noqa: F401
        RunOptions,  # noqa: F401
        SessionIOBinding,  # noqa: F401
        SessionOptions,  # noqa: F401
        create_and_register_allocator,  # noqa: F401
        create_and_register_allocator_v2,  # noqa: F401
        disable_telemetry_events,  # noqa: F401
        enable_telemetry_events,  # noqa: F401
        get_all_providers,  # noqa: F401
        get_available_providers,  # noqa: F401
        get_build_info,
        get_device,  # noqa: F401
        get_ep_devices,  # noqa: F401
        get_version_string,  # noqa: F401
        has_collective_ops,  # noqa: F401
        register_execution_provider_library,
        set_default_logger_severity,  # noqa: F401
        set_default_logger_verbosity,  # noqa: F401
        set_global_thread_pool_sizes,  # noqa: F401
        set_seed,  # noqa: F401
        unregister_executor_provider_library,  # noqa: F401
    )

    import_capi_exception = None
except Exception as e:
    import_capi_exception = e

from onnxruntime.capi import onnxruntime_validation

if import_capi_exception:
    raise import_capi_exception
