define({ "api": [  {    "type": "GET",    "url": "/swimmer/addlap/:id",    "title": "Increment Lap Count",    "name": "AddLap",    "group": "Swimmer",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Swimmer’s unique 3-digit ID</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "status",            "description": "<p>Response code of the request</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "msg",            "description": "<p>Description about the response</p>"          },          {            "group": "Success 200",            "type": "Dictionary",            "optional": false,            "field": "result",            "description": "<p>New information of the swimmer</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "result.id",            "description": "<p>Unique ID of swimmer</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "result.name",            "description": "<p>Name of swimmer</p>"          },          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "result.laps",            "description": "<p>Updated laps completed by swimmer</p>"          }        ]      }    },    "version": "0.0.0",    "filename": "apidoc/apidoc.py",    "groupTitle": "Swimmer",    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "0",            "description": "<p>Success.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "1",            "description": "<p>Swimmer <code>id</code> not found.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "8",            "description": "<p>Swimmer is not being recorded.</p>"          }        ]      }    }  },  {    "type": "GET",    "url": "/swimmer/avatar/:id",    "title": "Request Swimmer Avatar",    "name": "GetSwimmerAvatar",    "group": "Swimmer",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Swimmer’s unique 3-digit ID</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "Blob",            "optional": false,            "field": "N/A",            "description": "<p>Avatar of the requested swimmer</p>"          }        ]      }    },    "version": "0.0.0",    "filename": "apidoc/apidoc.py",    "groupTitle": "Swimmer",    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "0",            "description": "<p>Success.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "1",            "description": "<p>Swimmer <code>id</code> not found.</p>"          }        ]      }    }  },  {    "type": "GET",    "url": "/swimmer/info/:id",    "title": "Request Swimmer Information",    "name": "GetSwimmerInfo",    "group": "Swimmer",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Swimmer’s unique 3-digit ID</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "status",            "description": "<p>Response code of the request</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "msg",            "description": "<p>Description about the response</p>"          },          {            "group": "Success 200",            "type": "Dictionary",            "optional": false,            "field": "result",            "description": "<p>Information of the requested swimmer</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "result.id",            "description": "<p>Unique ID of swimmer</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "result.name",            "description": "<p>Name of swimmer</p>"          },          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "result.laps",            "description": "<p>Laps completed by swimmer</p>"          }        ]      },      "examples": [        {          "title": "Success Response",          "content": "{\n    \"status\": 0,\n    \"msg\": \"Success\",\n    \"result\": {\n        \"id\": \"001\",\n        \"name\": \"John Appleseed\",\n        \"laps\": 15\n    }\n}",          "type": "json"        }      ]    },    "version": "0.0.0",    "filename": "apidoc/apidoc.py",    "groupTitle": "Swimmer",    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "0",            "description": "<p>Success.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "1",            "description": "<p>Swimmer <code>id</code> not found.</p>"          }        ]      }    }  },  {    "type": "POST",    "url": "/swimmer/new",    "title": "Create New Swimmer",    "name": "NewSwimmer",    "group": "Swimmer",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Swimmer’s unique 3-digit ID</p>"          },          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "name",            "description": "<p>Swimmer’s name</p>"          },          {            "group": "Parameter",            "type": "Blob",            "optional": false,            "field": "avatar",            "description": "<p>Swimmer’s avatar image file in JPEG format</p>"          },          {            "group": "Parameter",            "type": "Integer",            "optional": false,            "field": "laps",            "description": "<p><em>(Optional. Default: 0)</em> Swimmer’s lap count (non-negative)</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "status",            "description": "<p>Response code of the request</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "msg",            "description": "<p>Description about the response</p>"          }        ]      }    },    "version": "0.0.0",    "filename": "apidoc/apidoc.py",    "groupTitle": "Swimmer",    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "0",            "description": "<p>Success.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "2",            "description": "<p>Invalid value for <code>laps</code> param.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "4",            "description": "<p>Missing value or file for new swimmer, requires <code>id</code>, <code>name</code> and <code>avatar</code>.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "5",            "description": "<p>Invalid swimmer <code>id</code>.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "6",            "description": "<p>Existing swimmer <code>id</code>.</p>"          }        ]      }    }  },  {    "type": "GET",    "url": "/swimmer/setlap/:id/:laps",    "title": "Set Lap Count",    "name": "SetLap",    "group": "Swimmer",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Swimmer’s unique 3-digit ID</p>"          },          {            "group": "Parameter",            "type": "Integer",            "optional": false,            "field": "laps",            "description": "<p>Swimmer’s new lap count (non-negative)</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "status",            "description": "<p>Response code of the request</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "msg",            "description": "<p>Description about the response</p>"          },          {            "group": "Success 200",            "type": "Dictionary",            "optional": false,            "field": "result",            "description": "<p>New information of the swimmer</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "result.id",            "description": "<p>Unique ID of swimmer</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "result.name",            "description": "<p>Name of swimmer</p>"          },          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "result.laps",            "description": "<p>Updated laps completed by swimmer</p>"          }        ]      }    },    "version": "0.0.0",    "filename": "apidoc/apidoc.py",    "groupTitle": "Swimmer",    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "0",            "description": "<p>Success.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "1",            "description": "<p>Swimmer <code>id</code> not found.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "2",            "description": "<p>Invalid value for <code>laps</code> param.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "8",            "description": "<p>Swimmer is not being recorded.</p>"          }        ]      }    }  },  {    "type": "GET",    "url": "/swimmer/start-record/:id",    "title": "Start Recording Swimmer",    "name": "StartRecordSwimmer",    "group": "Swimmer",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Swimmer’s unique 3-digit ID</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "status",            "description": "<p>Response code of the request</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "msg",            "description": "<p>Description about the response</p>"          }        ]      }    },    "version": "0.0.0",    "filename": "apidoc/apidoc.py",    "groupTitle": "Swimmer",    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "0",            "description": "<p>Success.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "1",            "description": "<p>Swimmer <code>id</code> not found.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "7",            "description": "<p>Swimmer already being recorded.</p>"          }        ]      }    }  },  {    "type": "GET",    "url": "/swimmer/stop-record/:id",    "title": "Stop Recording Swimmer",    "name": "StopRecordSwimmer",    "group": "Swimmer",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Swimmer’s unique 3-digit ID</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "status",            "description": "<p>Response code of the request</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "msg",            "description": "<p>Description about the response</p>"          }        ]      }    },    "version": "0.0.0",    "filename": "apidoc/apidoc.py",    "groupTitle": "Swimmer",    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "0",            "description": "<p>Success.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "1",            "description": "<p>Swimmer <code>id</code> not found.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "8",            "description": "<p>Swimmer is not being recorded.</p>"          }        ]      }    }  },  {    "type": "GET",    "url": "/swimmer/sublap/:id",    "title": "Decrement Lap Count",    "name": "SubtractLap",    "group": "Swimmer",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Swimmer’s unique 3-digit ID</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "status",            "description": "<p>Response code of the request</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "msg",            "description": "<p>Description about the response</p>"          },          {            "group": "Success 200",            "type": "Dictionary",            "optional": false,            "field": "result",            "description": "<p>New information of the swimmer</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "result.id",            "description": "<p>Unique ID of swimmer</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "result.name",            "description": "<p>Name of swimmer</p>"          },          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "result.laps",            "description": "<p>Updated laps completed by swimmer</p>"          }        ]      }    },    "version": "0.0.0",    "filename": "apidoc/apidoc.py",    "groupTitle": "Swimmer",    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "0",            "description": "<p>Success.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "1",            "description": "<p>Swimmer <code>id</code> not found.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "8",            "description": "<p>Swimmer is not being recorded.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "9",            "description": "<p>Already 0 laps.</p>"          }        ]      }    }  },  {    "type": "POST",    "url": "/swimmer/update/avatar",    "title": "Update Swimmer Avatar",    "name": "UpdateAvatar",    "group": "Swimmer",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Swimmer’s unique 3-digit ID</p>"          },          {            "group": "Parameter",            "type": "Blob",            "optional": false,            "field": "avatar",            "description": "<p>Swimmer’s avatar image file in JPEG format</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "Integer",            "optional": false,            "field": "status",            "description": "<p>Response code of the request</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "msg",            "description": "<p>Description about the response</p>"          }        ]      }    },    "version": "0.0.0",    "filename": "apidoc/apidoc.py",    "groupTitle": "Swimmer",    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "0",            "description": "<p>Success.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "1",            "description": "<p>Swimmer <code>id</code> not found.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "5",            "description": "<p>Invalid swimmer <code>id</code>.</p>"          },          {            "group": "Error 4xx",            "optional": false,            "field": "10",            "description": "<p>Missing value or file for updating swimmer's avatar, requires <code>id</code> and <code>avatar</code>.</p>"          }        ]      }    }  },  {    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "optional": false,            "field": "varname1",            "description": "<p>No type.</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "varname2",            "description": "<p>With type.</p>"          }        ]      }    },    "type": "",    "url": "",    "version": "0.0.0",    "filename": "apidoc/apidoc/main.js",    "group": "_Users_GeorgeYu_Desktop_swim4love_server_apidoc_apidoc_main_js",    "groupTitle": "_Users_GeorgeYu_Desktop_swim4love_server_apidoc_apidoc_main_js",    "name": ""  },  {    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "optional": false,            "field": "varname1",            "description": "<p>No type.</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "varname2",            "description": "<p>With type.</p>"          }        ]      }    },    "type": "",    "url": "",    "version": "0.0.0",    "filename": "apidoc/apidoc-template 2/main.js",    "group": "_Users_GeorgeYu_Desktop_swim4love_server_apidoc_apidoc_template_2_main_js",    "groupTitle": "_Users_GeorgeYu_Desktop_swim4love_server_apidoc_apidoc_template_2_main_js",    "name": ""  },  {    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "optional": false,            "field": "varname1",            "description": "<p>No type.</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "varname2",            "description": "<p>With type.</p>"          }        ]      }    },    "type": "",    "url": "",    "version": "0.0.0",    "filename": "apidoc/apidoc-template/main.js",    "group": "_Users_GeorgeYu_Desktop_swim4love_server_apidoc_apidoc_template_main_js",    "groupTitle": "_Users_GeorgeYu_Desktop_swim4love_server_apidoc_apidoc_template_main_js",    "name": ""  }] });
