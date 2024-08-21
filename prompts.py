
FLUX_SIMPLE_PROMPT = """
{
  "6": {
    "inputs": {
      "text": [
        "40",
        0
      ],
      "clip": [
        "11",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Positive Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "46",
        0
      ],
      "vae": [
        "10",
        0
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "10": {
    "inputs": {
      "vae_name": "ae.sft"
    },
    "class_type": "VAELoader",
    "_meta": {
      "title": "Load VAE"
    }
  },
  "11": {
    "inputs": {
      "clip_name1": "t5xxl_fp16.safetensors",
      "clip_name2": "clip_l.safetensors",
      "type": "flux"
    },
    "class_type": "DualCLIPLoader",
    "_meta": {
      "title": "DualCLIPLoader"
    }
  },
  "27": {
    "inputs": {
      "width": 1024,
      "height": 768,
      "batch_size": 1
    },
    "class_type": "EmptySD3LatentImage",
    "_meta": {
      "title": "EmptySD3LatentImage"
    }
  },
  "40": {
    "inputs": {
      "prompt": "1girl, 1cat"
    },
    "class_type": "CR Prompt Text",
    "_meta": {
      "title": "Positive Prompt"
    }
  },
  "41": {
    "inputs": {
      "prompt": ""
    },
    "class_type": "CR Prompt Text",
    "_meta": {
      "title": "Negative Prompt"
    }
  },
  "43": {
    "inputs": {
      "format": "webp",
      "lossless_webp": true,
      "compression": 80,
      "save_tags": "None",
      "filename_template": "{model}",
      "eagle_folder": "",
      "positive": [
        "40",
        0
      ],
      "negative": [
        "41",
        0
      ],
      "memo_text": "",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "D2 Send Eagle",
    "_meta": {
      "title": "D2 Send Eagle"
    }
  },
  "44": {
    "inputs": {
      "unet_name": "FusionDS_v0_Q8.gguf"
    },
    "class_type": "UnetLoaderGGUF",
    "_meta": {
      "title": "Unet Loader (GGUF)"
    }
  },
  "46": {
    "inputs": {
      "seed": 672655501467235,
      "steps": 4,
      "cfg": 1,
      "sampler_name": "euler",
      "scheduler": "simple",
      "denoise": 1,
      "model": [
        "44",
        0
      ],
      "positive": [
        "6",
        0
      ],
      "negative": [
        "48",
        0
      ],
      "latent_image": [
        "27",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "48": {
    "inputs": {
      "text": [
        "41",
        0
      ],
      "clip": [
        "11",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Negative Prompt)"
    }
  },
  "save_image_websocket_node": {
    "inputs": {
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImageWebsocket",
    "_meta": {
      "title": "SaveImageWebsocket"
    }
  }
}
"""


