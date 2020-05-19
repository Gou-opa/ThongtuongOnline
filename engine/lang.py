# -*- coding: utf-8 -*-
class Lang:
    line_break = "- - - - - - - -"
    hello = "____{}____"
    prompt = "{}: "
    prompt_with_current = "{}[{}]: "
    class vi:
        welcome = "Thống tướng Online"
        farewell = "Đóng Thống tướng Online"

        class cli:
            hello = "CLI"
            action = "Hành động/số chỉ"
            class help:
                hello = "Danh mục hành động"
            class language:
                hello = "Danh mục hành động"
                change_lang_prompt = "Chọn ngôn ngữ"
                change_failed = "Không tìm thấy ngôn ngữ"
                apply_lang = "Lựa chọn ngôn ngữ Tiếng Việt"
            class login:
                failed = "Sai tên đăng nhập hoặc mật khẩu"
                hello = "Đăng nhập vào tài khoản Thống tướng Online của bạn"
                username_prompt = "Tên đăng nhập Thống tướng"
                password_prompt = "Mật khẩu của bạn"
            class register:
                hello = "Tạo tài khoản Thống tướng Online mới"
                username_prompt = "Tên đăng nhập Thống tướng"
                password_prompt = "Mật khẩu của bạn"
            class commands:
                not_exist = "Hành động không đúng, mời thử lại"

                help_command = "Trợ giúp"
                help_desc = "Hiển thị hướng dẫn cho các hành động"

                login_command = "Đăng nhập"
                login_desc = "Đăng nhập bằng tên đăng nhập và mật khẩu của bạn"

                register_command = "Tạo tài khoản"
                register_desc = "Tạo tài khoản mới"

                change_lang_command = "Đổi ngôn ngữ"
                change_lang_desc = "Chọn ngôn ngữ mới, sử dụng mã viết tắt 2 chữ cái của ngôn ngữ"

                exit_command = "Thoát"
                exit_desc = "Thoát game"
    class en:
        pass

    content = {"en": en, "vi": vi}