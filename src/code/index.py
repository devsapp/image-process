# -*- coding: utf-8 -*-

import oss2
import json
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import base64


def oss_get_image_data(context, path):
    parts = path.split("/")
    bucket = parts[0]
    object = "/".join(parts[1:])
    creds = context.credentials
    auth = oss2.StsAuth(creds.accessKeyId, creds.accessKeySecret, creds.securityToken)
    oss_client = oss2.Bucket(
        auth, "oss-" + context.region + "-internal.aliyuncs.com", bucket
    )
    return oss_client.get_object(object)


def oss_save_image_data(context, img_blob, path):
    parts = path.split("/")
    bucket = parts[0]
    object = "/".join(parts[1:])
    creds = context.credentials
    auth = oss2.StsAuth(creds.accessKeyId, creds.accessKeySecret, creds.securityToken)
    oss_client = oss2.Bucket(
        auth, "oss-" + context.region + "-internal.aliyuncs.com", bucket
    )
    print(bucket, object)
    oss_client.put_object(object, img_blob)


def pinjie(query, context):
    try:
        image1 = query.get("left")
        image2 = query.get("right")
        assert image1 and image2
        fmt = query.get("fmt", "jpg")
        print("pinjie images: ", image1, image2)
        with Image(file=oss_get_image_data(context, image1)) as f1:
            with Image(file=oss_get_image_data(context, image2)) as f2:
                with Image(
                    width=f1.width + f2.width + 10, height=max(f1.height, f2.height)
                ) as img:
                    img.format = fmt
                    img.composite(f1, left=0, top=0)
                    img.composite(f2, left=f1.width + 10, top=0)
                    return make_response(context, query, img.make_blob(), fmt)
    except Exception as ex:
        return make_error_response(ex)


def watermark(query, context):
    try:
        image = query.get("img")
        text = query.get("text")
        assert image and text
        fmt = query.get("fmt", "jpg")
        print("watermark image: {}, text: {}".format(image, text))
        with Drawing() as draw:
            draw.font = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
            draw.fill_color = Color("red")
            draw.font_size = 24
            with Image(width=200, height=50, background=Color("transparent")) as pic:
                draw.text(10, int(pic.height / 2), text)
                draw(pic)
                pic.alpha = True
                pic.format = "png"
                pic.save(filename="/tmp/water.png")

        with Image(file=oss_get_image_data(context, image)) as img:
            with Image(filename="/tmp/water.png") as water:
                with img.clone() as base:
                    base.format = fmt
                    base.watermark(water, 0.3, 0, int(img.height - 30))
                    return make_response(context, query, base.make_blob(), fmt)
    except Exception as ex:
        return make_error_response(ex)


def format(query, context):
    try:
        image = query.get("img")
        fmt = query.get("fmt")
        assert image and fmt
        print("format image: {}, fmt: {}".format(image, fmt))
        with Image(file=oss_get_image_data(context, image)) as img:
            img.format = fmt
            return make_response(context, query, img.make_blob(), fmt)
    except Exception as ex:
        return make_error_response(ex)


def gray(query, context):
    try:
        img_path = query.get("img")
        parts = img_path.split("/")
        object = "/".join(parts[1:])
        img_type = object.split(".")[-1]
        if (
            img_type != "jpg"
            and img_type != "jpeg"
            and img_type != "webp"
            and img_type != "png"
        ):
            img_type = "jpeg"

        with Image(file=oss_get_image_data(context, img_path)) as img:
            img.format = img_type
            img.transform_colorspace("gray")
            return make_response(context, query, img.make_blob(), img_type)
    except Exception as ex:
        return make_error_response(ex)


def make_error_response(ex):
    return {
        "body": "ERROR: {}".format(str(ex)),
        "headers": {"content-type": "text/plain"},
        "statusCode": 500,
    }


def make_response(context, query, img_blob, img_type):
    target = query.get("target")
    if target is not None and len(target) > 0:
        oss_save_image_data(context, img_blob, target)
    base64Data = base64.b64encode(img_blob).decode()
    dataUrl = "data:image/{};base64,{}".format(img_type, base64Data)
    html = """
<div style="text-align: center;">
<img src="{}" alt="Base64 Image" style="display: inline-block;">
</div>
""".format(
        dataUrl
    )
    return {
        "body": html,
        "headers": {"content-type": "text/html"},
        "statusCode": 200,
    }


def handler(event, context):
    evt = json.loads(event)
    print(evt)
    path = evt["requestContext"]["http"]["path"]
    method = evt["requestContext"]["http"]["method"]
    query = evt.get("queryParameters", {})
    if method != "GET":
        return {
            "body": "only support GET method\n",
            "statusCode": 200,
        }

    if path == "/gray":
        return gray(query, context)

    elif path == "/format":
        return format(query, context)

    elif path == "/watermark":
        return watermark(query, context)

    elif path == "/pinjie":
        return pinjie(query, context)

    else:
        with open("index.html") as f:
            return {
                "body": f.read(),
                "headers": {"content-type": "text/html"},
                "statusCode": 200,
            }
