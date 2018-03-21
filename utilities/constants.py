class Constants:
    ACTIVE = 1
    INACTIVE = 0
    INPUT_DEVICE = 1
    OUTPUT_DEVICE = 2
    IN_OUTPUT_DEVICE = 3
    SUCCESS_UPDATE_MESSAGE = 'was updated correctly'
    SUCCESS_CREATE_MESSAGE = 'was created correctly'
    DAILY_ACTIVITIES = 1
    REALISTIC = 2
    IMAGINARY = 3
    ABSTRACT = 4
    REACHED_ANGLE = 1
    NONE = 0
    BEHAVIORAL = 'behavioral'
    COGNITIVE = 'cognitive'
    WIDE_PHYSICAL = 'wide_physical'
    TIGHT_PHYSICAL = 'tight_physical'
    CONSTANT_SUPER = 'constant_supervision'
    ADAPTATION = 'adaptation'
    ASYNC_SUPERVISION = 'async_supervision'
    NO_SUPERVISION = 'no_supervision'
    GAME_STATUS = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    DEVICE_TYPE = (
        (INPUT_DEVICE, 'Input'),
        (OUTPUT_DEVICE, 'Output'),
        (IN_OUTPUT_DEVICE, 'Input/Output'),
    )
    THEMATIC_CONTENT = (
        (DAILY_ACTIVITIES, 'Daily Life Activities'),
        (REALISTIC, 'Realistic'),
        (IMAGINARY, 'Imaginary'),
        (ABSTRACT, 'Abstract'),
    )
    PERFORMANCE_MEASURE = (
        (REACHED_ANGLE, 'Reached Angle'),
        (NONE, 'None'),
    )
    REHABILITATION_TYPE = (
        (WIDE_PHYSICAL, 'Physical - Wide Focus'),
        (TIGHT_PHYSICAL, 'Wide Focus - Tight Focus'),
        (BEHAVIORAL, 'Behavioral'),
        (COGNITIVE, 'Cognitive'),
    )
    AUTONOMY_DEGREE = (
        (CONSTANT_SUPER, '1. Only motivates, requires constant physiotherapist supervision'),
        (ADAPTATION, '2. Provides adaptation features or constraints motion, requires constant physiotherapist supervision'),
        (ASYNC_SUPERVISION , '3. Requires asynchronous physiotherapist supervision remotely or along periodic meetings'),
        (NO_SUPERVISION , '4. Standalone, does not require physiotherapist supervision'),
    )