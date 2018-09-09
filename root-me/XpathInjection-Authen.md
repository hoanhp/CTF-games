Tương tự như SQL injection, XPath injection xảy ra khi website sử dụng thông tin do người dùng cung cấp để xây dựng câu truy vấn cho XPath
cho dữ liệu XML
Ví dụ về câu truy vấn trong XPath:
VB: Dim FindUserXPath as String FindUserXPath = "//Employee[UserName/text()='" & Request("Username").Replace("'", "&apos;") & "' And Password/text()='" & Request("Password").Replace("'", "&apos;") & "']" C#: String FindUserXPath; FindUserXPath = "//Employee[UserName/text()='" + Request("Username").Replace("'", "&apos;") + "' And Password/text()='" + Request("Password").Replace("'", "&apos;") + "']";

=> đã tìm được tài khoản admin có usernam là JOHN => đặt username cho XPATH injection là: JOHN' or '1' = '1

