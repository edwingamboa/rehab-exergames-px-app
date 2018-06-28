class Constants:
    ACTIVE = 1
    INACTIVE = 0
    INPUT_DEVICE = 1
    OUTPUT_DEVICE = 2
    IN_OUTPUT_DEVICE = 3
    SUCCESS_UPDATE_MESSAGE = 'was updated correctly'
    SUCCESS_CREATE_MESSAGE = 'was created correctly'
    SUCCESS_INIT_MESSAGE = 'creation initiated correctly'
    SUCCESS_CONTINUE_MESSAGE = 'creation continued correctly'
    # Thematic content
    DAILY_ACTIVITIES = 1
    REALISTIC = 2
    IMAGINARY = 3
    ABSTRACT = 4
    # Performance measure
    REACHED_ANGLE = 1
    NONE = 0
    # Rehabilitation types
    BEHAVIORAL = 'behavioral'
    COGNITIVE = 'cognitive'
    WIDE_PHYSICAL = 'wide_physical'
    TIGHT_PHYSICAL = 'tight_physical'
    # Autonomy degrees
    CONSTANT_SUPER = 'constant_supervision'
    ADAPTATION = 'adaptation'
    ASYNC_SUPERVISION = 'async_supervision'
    NO_SUPERVISION = 'no_supervision'
    # Evaluation stages
    ENV_ANALYSIS = 'rehab_env_analysis'
    EVAL_GOAL_DEF = 'eval_goal_def'
    ASPECTS_SEL = 'aspects_sel'
    METHODS_SEL = 'methods_sel'
    INSTRUMENTS_SEL = 'instruments_sel'
    EVAL_PREP = 'eval_prep'
    EVAL = 'eval'
    REPORT = 'report'
    # Questionnaire status
    INIT = 'init'
    IN_DESIGN = 'in_design'
    IN_PRE_TEST = 'in_pre_test'
    FINISHED = 'finished'
    IN_REVIEW = 'in_review'
    # Questionnaire measures types
    VALIDITY = 'validity'
    RELIABILITY = 'reliability'
    # Lists
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
        (WIDE_PHYSICAL, 'Wide Focus'),
        (TIGHT_PHYSICAL, 'Tight Focus'),
    )
    AUTONOMY_DEGREE = (
        (CONSTANT_SUPER, '1. Only motivates, requires constant physiotherapist supervision'),
        (ADAPTATION, '2. Provides adaptation features or constraints motion, requires constant physiotherapist supervision'),
        (ASYNC_SUPERVISION , '3. Requires asynchronous physiotherapist supervision remotely or along periodic meetings'),
        (NO_SUPERVISION , '4. Standalone, does not require physiotherapist supervision'),
    )
    EVALUATION_STAGE = (
        (ENV_ANALYSIS, 'Rehabilitation Environment Analysis'),
        (EVAL_GOAL_DEF, 'Evaluation Goal Definition'),
        (ASPECTS_SEL, 'Evaluation Aspects Selection'),
        (METHODS_SEL, 'Evaluation Methods Selection'),
        (INSTRUMENTS_SEL, 'Evaluation Instruments Selection'),
        (EVAL_PREP, 'Evaluation Preparation'),
        # (EVAL, 'Evaluation'),
        (REPORT, 'Results Analysis and Reporting'),
        (FINISHED, 'Finished'),
    )
    QUESTIONNAIRE_STATUS = (
        (INIT,  'Initiated'),
        (IN_DESIGN,  'In Design'),
        (IN_PRE_TEST,  'In Pre-Testing'),
        (FINISHED,  'Finished'),
        (IN_REVIEW,  'In Review'),
    )
    QUESTIONNAIRE_MEASURE_TYPES = (
        (VALIDITY,  'Validity'),
        (RELIABILITY,  'Reliability'),
    )