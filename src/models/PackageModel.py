from pydantic import Field, validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config




class InputImageTwo(Input):
    name: Literal["inputImageTwo"] = "inputImageTwo"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"
        return "object"

    class Config:
        title = "Image"


class InputImageOne(Input):
    name: Literal["inputImageOne"] = "inputImageOne"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"
        return "object"

    class Config:
        title = "Image"


class OutputImageTwo(Output):
    name: Literal["outputImageTwo"] = "outputImageTwo"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"
        return "object"

    class Config:
        title = "Image"


class OutputImageOne(Output):
    name: Literal["outputImageOne"] = "outputImageOne"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"
        return "object"

    class Config:
        title = "Image"


class ThresholdValue(Config):
    name: Literal["ThresholdValue"] = "ThresholdValue"
    value: int = Field(default=127, ge=0, le=255)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Threshold Value"


class Alpha(Config):
    name: Literal["Alpha"] = "Alpha"
    value: float
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Alpha"


class OptionEnable(Config):
    name: Literal["OptionEnable"] = "OptionEnable"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Enable"


class OptionDisable(Config):
    name: Literal["OptionDisable"] = "OptionDisable"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disable"


class Invert(Config):
    name: Literal["Invert"] = "Invert"
    value: Union[OptionEnable, OptionDisable]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Invert"


class NormalizeOutput(Config):
    name: Literal["NormalizeOutput"] = "NormalizeOutput"
    value: Union[OptionEnable, OptionDisable]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Normalize Output"


class ThresholdMethod(Config):
    thresholdValue: ThresholdValue
    invert: Invert

    name: Literal["ThresholdMethod"] = "ThresholdMethod"
    value: Literal["Threshold"] = "Threshold"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Threshold"


class NormalizeMethod(Config):
    alpha: Alpha
    normalizeOutput: NormalizeOutput

    name: Literal["NormalizeMethod"] = "NormalizeMethod"
    value: Literal["Normalize"] = "Normalize"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Normalize"


class DifferenceMethod(Config):
    name: Literal["DifferenceMethod"] = "DifferenceMethod"
    value: Union[ThresholdMethod, NormalizeMethod]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Method"


class DifferenceExecutorInputs(Inputs):
    inputImageOne: InputImageOne
    inputImageTwo: InputImageTwo


class DifferenceExecutorConfigs(Configs):
    differenceMethod: DifferenceMethod


class DifferenceExecutorRequest(Request):
    inputs: Optional[DifferenceExecutorInputs]
    configs: DifferenceExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class DifferenceExecutorOutputs(Outputs):
    outputImageOne: OutputImageOne
    outputImageTwo: OutputImageTwo


class DifferenceExecutorResponse(Response):
    outputs: DifferenceExecutorOutputs


class DifferenceExecutor(Config):
    name: Literal["DifferenceExecutor"] = "DifferenceExecutor"
    value: Union[DifferenceExecutorRequest, DifferenceExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "DifferenceExecutor"
        json_schema_extra = {
            "target": {
                "value": 1
            }
        }


class ScaleX(Config):
    name: Literal["ScaleX"] = "ScaleX"
    value: float
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Scale X"


class ScaleY(Config):
    name: Literal["ScaleY"] = "ScaleY"
    value: float
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Scale Y"


class Width(Config):
    name: Literal["Width"] = "Width"
    value: int
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Width"


class Height(Config):
    name: Literal["Height"] = "Height"
    value: int
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Height"


class ConfigScale(Config):
    name: Literal["ConfigScale"] = "ConfigScale"

    scaleX: ScaleX
    scaleY: ScaleY

    value: Literal["Scale"] = "Scale"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Scale"


class ConfigCustomSize(Config):
    name: Literal["ConfigCustomSize"] = "ConfigCustomSize"

    width: Width
    height: Height

    value: Literal["CustomSize"] = "CustomSize"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Custom Size"


class ResizeMethod(Config):
    name: Literal["ResizeMethod"] = "ResizeMethod"
    value: Union[ConfigScale, ConfigCustomSize]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Resize Method"


class ResizeExecutorInputs(Inputs):
    inputImageOne: InputImageOne


class ResizeExecutorConfigs(Configs):
    resizeMethod: ResizeMethod


class ResizeExecutorRequest(Request):
    inputs: Optional[ResizeExecutorInputs]
    configs: ResizeExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class ResizeExecutorOutputs(Outputs):
    outputImageOne: OutputImageOne


class ResizeExecutorResponse(Response):
    outputs: ResizeExecutorOutputs


class ResizeExecutor(Config):
    name: Literal["ResizeExecutor"] = "ResizeExecutor"
    value: Union[ResizeExecutorRequest, ResizeExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "ResizeExecutor"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[ResizeExecutor, DifferenceExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["FirstDemoPackage"] = "FirstDemoPackage"