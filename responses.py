history = {
    200: 
    {
     "content": 
     {
      "application/json": 
      {
       "example": 
        [
            {
            "address": "mc.example.com",
            "playername": "Nucceteere",
            "playeruuid": "1f8a091c-3daa-4dbd-a15f-a3753a6f36b3",
            "lastseen": 1733107822
            },
            {
            "address": "mc.example.com",
             "playername": "Nucceteere",
             "playeruuid": "1f8a091c-3daa-4dbd-a15f-a3753a6f36b3",
             "lastseen": 1731888338
            }
        ]
       }
      }, 
        "description": "Return Player History"
    },

    422: 
    {
     "content": 
     {
      "application/json": 
      {
        "example": 
       {
        "detail": "You can't use both player and address!"
       }
      }
     }
     , "description": "Unprocessable Content"
    }
}

stats = {
    200: 
    {
     "content": 
     {
      "application/json": 
      {
        "example": 
       {
        "servers": "250863"
       }
      }
     }
     , "description": "Return Stats"
    }
}