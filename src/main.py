import logging
from frontend.token.Lexer import Lexer
from frontend.parse.parser import Parser

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def main():
    # 소스 코드 파일 경로
    file_path = 'source.txt'

    # 파일에서 소스 코드 읽기
    with open(file_path, 'r') as file:
        source_code = file.read()

    # Lexer 초기화 및 토큰 생성
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    # Parser 초기화 및 구문 분석
    parser = Parser(tokens)
    ast = parser.parse()

    # 추후 추가 동작 예시 (예: AST 실행, 결과 출력 등)
    print(ast)

if __name__ == '__main__':
    main()
