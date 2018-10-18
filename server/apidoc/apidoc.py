"""
@apiDefine Success
@apiError 0 Success.
"""
"""
@apiDefine IdNotFound
@apiError 1 Swimmer <code>id</code> not found.
"""
"""
@apiDefine InvalidParamLaps
@apiError 2 Invalid value for <code>laps</code> param.
"""
"""
@apiDefine AvatarNotFound
@apiError 3 Swimmer avatar file not found.
"""
"""
@apiDefine MissingParamNewSwimmer
@apiError 4 Missing value or file for new swimmer, requires <code>id</code>, <code>name</code> and <code>avatar</code>.
"""
"""
@apiDefine InvalidId
@apiError 5 Invalid swimmer <code>id</code>.
"""
"""
@apiDefine ExistingId
@apiError 6 Existing swimmer <code>id</code>.
"""
"""
@apiDefine AlreadyRecording
@apiError 7 Swimmer already being recorded.
"""
"""
@apiDefine NotRecording
@apiError 8 Swimmer is not being recorded.
"""
"""
@apiDefine AlreadyZeroLaps
@apiError 9 Already 0 laps.
"""
"""
@apiDefine MissingParamUpdateAvatar
@apiError 10 Missing value or file for updating swimmer\'s avatar, requires <code>id</code> and <code>avatar</code>.
"""

"""
@api {GET} /swimmer/info/:id Request Swimmer Information
@apiName GetSwimmerInfo
@apiGroup Swimmer

@apiParam {String} id Swimmer’s unique 3-digit ID

@apiUse Success
@apiUse IdNotFound

@apiSuccess {Integer} status Response code of the request
@apiSuccess {String} msg Description about the response
@apiSuccess {Dictionary} result Information of the requested swimmer
@apiSuccess {String} result.id Unique ID of swimmer
@apiSuccess {String} result.name Name of swimmer
@apiSuccess {Integer} result.laps Laps completed by swimmer

@apiSuccessExample {json} Success Response
    {
        "status": 0,
        "msg": "Success",
        "result": {
            "id": "001",
            "name": "John Appleseed",
            "laps": 15
        }
    }
"""

"""
@api {GET} /swimmer/avatar/:id Request Swimmer Avatar
@apiName GetSwimmerAvatar
@apiGroup Swimmer

@apiParam {String} id Swimmer’s unique 3-digit ID

@apiUse Success
@apiUse IdNotFound

@apiSuccess {Blob} N/A Avatar of the requested swimmer
"""

"""
@api {GET} /swimmer/start-record/:id Start Recording Swimmer
@apiName StartRecordSwimmer
@apiGroup Swimmer

@apiParam {String} id Swimmer’s unique 3-digit ID

@apiUse Success
@apiUse IdNotFound
@apiUse AlreadyRecording

@apiSuccess {Integer} status Response code of the request
@apiSuccess {String} msg Description about the response
"""

"""
@api {GET} /swimmer/stop-record/:id Stop Recording Swimmer
@apiName StopRecordSwimmer
@apiGroup Swimmer

@apiParam {String} id Swimmer’s unique 3-digit ID

@apiUse Success
@apiUse IdNotFound
@apiUse NotRecording

@apiSuccess {Integer} status Response code of the request
@apiSuccess {String} msg Description about the response
"""

"""
@api {GET} /swimmer/addlap/:id Increment Lap Count
@apiName AddLap
@apiGroup Swimmer

@apiParam {String} id Swimmer’s unique 3-digit ID

@apiUse Success
@apiUse IdNotFound
@apiUse NotRecording

@apiSuccess {Integer} status Response code of the request
@apiSuccess {String} msg Description about the response
@apiSuccess {Dictionary} result New information of the swimmer
@apiSuccess {String} result.id Unique ID of swimmer
@apiSuccess {String} result.name Name of swimmer
@apiSuccess {Integer} result.laps Updated laps completed by swimmer
"""

"""
@api {GET} /swimmer/sublap/:id Decrement Lap Count
@apiName SubtractLap
@apiGroup Swimmer

@apiParam {String} id Swimmer’s unique 3-digit ID

@apiUse Success
@apiUse IdNotFound
@apiUse NotRecording
@apiUse AlreadyZeroLaps

@apiSuccess {Integer} status Response code of the request
@apiSuccess {String} msg Description about the response
@apiSuccess {Dictionary} result New information of the swimmer
@apiSuccess {String} result.id Unique ID of swimmer
@apiSuccess {String} result.name Name of swimmer
@apiSuccess {Integer} result.laps Updated laps completed by swimmer
"""

"""
@api {GET} /swimmer/setlap/:id/:laps Set Lap Count
@apiName SetLap
@apiGroup Swimmer

@apiParam {String} id Swimmer’s unique 3-digit ID
@apiParam {Integer} laps Swimmer’s new lap count (non-negative)

@apiUse Success
@apiUse IdNotFound
@apiUse InvalidParamLaps
@apiUse NotRecording

@apiSuccess {Integer} status Response code of the request
@apiSuccess {String} msg Description about the response
@apiSuccess {Dictionary} result New information of the swimmer
@apiSuccess {String} result.id Unique ID of swimmer
@apiSuccess {String} result.name Name of swimmer
@apiSuccess {Integer} result.laps Updated laps completed by swimmer
"""

"""
@api {POST} /swimmer/new Create New Swimmer
@apiName NewSwimmer
@apiGroup Swimmer

@apiParam {String} id Swimmer’s unique 3-digit ID
@apiParam {String} name Swimmer’s name
@apiParam {Blob} avatar Swimmer’s avatar image file in JPEG format
@apiParam {Integer} laps <em>(Optional. Default: 0)</em> Swimmer’s lap count (non-negative)

@apiUse Success
@apiUse InvalidParamLaps
@apiUse MissingParamNewSwimmer
@apiUse InvalidId
@apiUse ExistingId

@apiSuccess {Integer} status Response code of the request
@apiSuccess {String} msg Description about the response
"""

"""
@api {POST} /swimmer/update/avatar Update Swimmer Avatar
@apiName UpdateAvatar
@apiGroup Swimmer

@apiParam {String} id Swimmer’s unique 3-digit ID
@apiParam {Blob} avatar Swimmer’s avatar image file in JPEG format

@apiUse Success
@apiUse IdNotFound
@apiUse InvalidId
@apiUse MissingParamUpdateAvatar

@apiSuccess {Integer} status Response code of the request
@apiSuccess {String} msg Description about the response
"""
