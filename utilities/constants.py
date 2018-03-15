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