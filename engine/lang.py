# -*- coding: utf-8 -*-
class Lang:
    line_break = "- - - - - - - -"
    hello = "____{}____"
    prompt = "{}: "
    prompt_with_current = "{}[{}]: "
    message_value = "{} [{}]"
    class vi:
        reload_game = "Có lỗi trong quá trình chạy game, tải lại"
        class window:
            exit_command = "Trở về"
            exit_desc = "Trở về giao diện trước"
            not_exist = "Hành động không đúng, mời thử lại"
            action = "Hành động/số chỉ"

        class welcome:
            farewell = "Đóng Thống tướng Online"
            hello = "Thống tướng Online"
        class setting:
            command = "Cài đặt"
            desc = "Cài đặt trò chơi"
            hello = "Cài đặt trò chơi"
            save = "Lưu cài đặt"
        class game:
            hello = "Báo cáo liên hành tinh"
            logout = "Thoát tài khoản Thống tướng Online"
            class economy:
                hello = "Tình hình kinh tế"
                display = "Tài chính: ${} (+${}/ngày)"
            class weapon:
                hello = "Tình hình vũ khí"
            class building:
                hello = "Tình hình cơ sở hạ tầng"
        class help:
            hello = "Danh mục hành động"
            command = "Trợ giúp"
            desc = "Hiển thị hướng dẫn cho các hành động"
        class language:
            hello = "Danh mục hành động"
            change_lang_prompt = "Chọn ngôn ngữ"
            change_failed = "Không tìm thấy ngôn ngữ"
            apply_lang = "Lựa chọn ngôn ngữ Tiếng Việt"
            command = "Đổi ngôn ngữ"
            desc = "Chọn ngôn ngữ mới, sử dụng mã viết tắt 2 chữ cái của ngôn ngữ"
        class login:
            failed = "Sai tên đăng nhập hoặc mật khẩu"
            hello = "Đăng nhập vào tài khoản Thống tướng Online của bạn"
            command = "Đăng nhập"
            desc = "Đăng nhập bằng tên đăng nhập và mật khẩu của bạn"
            username_prompt = "Tên đăng nhập Thống tướng"
            password_prompt = "Mật khẩu của bạn"
        class register:
            hello = "Tạo tài khoản Thống tướng Online mới"
            username_prompt = "Tên đăng nhập Thống tướng"
            password_prompt = "Mật khẩu của bạn"
            command = "Tạo tài khoản"
            desc = "Tạo tài khoản mới"
            ok = "Đăng ký thành công tài khoản"
            fail = "Đăng ký thất bại, sử dụng tên đăng nhập khác hoặc thử lại sau"

    class en:
        pass
    content = {"en": en, "vi": vi}