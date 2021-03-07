from util import HttpError

error400 = HttpError(400, "用户名或密码不能为空")
error401 = HttpError(401, "用户未登录")
error402 = HttpError(402, "请先注销当前用户")
error406 = HttpError(406, "用户名已存在")
error407 = HttpError(407, "昵称已存在")
error408 = HttpError(408, "用户名或密码错误")
error409 = HttpError(409, "该留言板不存在")
error410 = HttpError(410, "留言板内容为空")
error411 = HttpError(411, "字数超出上限")
error412 = HttpError(412, "未指定留言板id")
# error500 = HttpError(500, "servererror")
