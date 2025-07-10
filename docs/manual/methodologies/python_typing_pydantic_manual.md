# Python型アノテーションとPydantic活用マニュアル

## 1. はじめに

このマニュアルは、Pythonにおける型アノテーション（Type Annotation）の基本と、データバリデーションライブラリであるPydanticの活用方法について解説します。型アノテーションを導入することで、コードの可読性や保守性が向上し、静的解析ツールによるバグの早期発見が可能になります。

## 2. Pythonの基本的な型アノテーション

Python 3.5以降、変数や関数の引数、戻り値に対して型を付与できるようになりました。

### 2.1. 基本的な型

基本的な組み込み型（`int`, `str`, `float`, `bool`, `list`, `dict`など）を使ってアノテーションを行います。

```python
name: str = "Taro"
age: int = 30
is_active: bool = True
scores: list = [88, 92, 75]
```

### 2.2. `typing`モジュール

より複雑な型を表現するために、`typing`モジュールを利用します。

- `List`, `Tuple`, `Dict`, `Set`: ジェネリックコンテナ型
- `Optional`: `None`を取りうる値
- `Any`: 任意の型
- `Union`: 複数の型を取りうる値

```python
from typing import List, Dict, Optional, Tuple, Any, Union

# 文字列のリスト
names: List[str] = ["Taro", "Jiro"]

# キーが文字列、値が整数の辞書
user_ages: Dict[str, int] = {"Taro": 30, "Jiro": 25}

# Noneまたは文字列
nickname: Optional[str] = None

# 整数または文字列
identifier: Union[int, str] = "user-001"

# 任意の型
anything: Any = "hello"
```

## 3. Pydanticによるデータバリデーション

Pydanticは、型アノテーションを利用してデータのバリデーション、シリアライゼーション、ドキュメンテーションを強力にサポートするライブラリです。

### 3.1. インストール

`uv`環境下では、以下のコマンドでインストールします。

```bash
uv pip install pydantic
```

### 3.2. 基本的なモデルの作成

`pydantic.BaseModel`を継承してクラスを作成することで、データモデルを定義します。

```python
from pydantic import BaseModel, Field
from typing import List, Optional

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Optional[str] = None
    friends: List[int] = []

# データのインスタンス化
external_data = {
    "id": 123,
    "signup_ts": "2025-07-10T12:00:00",
    "friends": [1, "2", 3] # "2"はintに型強制される
}

user = User(**external_data)

print(user)
#> id=123 name='John Doe' signup_ts='2025-07-10T12:00:00' friends=[1, 2, 3]
print(user.id)
#> 123
```

Pydanticは、型アノテーションに基づいて自動的にデータの型変換（Coercion）とバリデーションを実行します。不正なデータが渡された場合は、`ValidationError`例外が発生します。

### 3.3. 高度なバリデーション

`Field`や`validator`デコレータを使用することで、より詳細なバリデーションルールを定義できます。

```python
from pydantic import BaseModel, Field, validator
from typing import List

class Item(BaseModel):
    name: str
    # 5文字以上、10文字以下の文字列
    description: str = Field(..., min_length=5, max_length=10)
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tags: List[str] = []

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

# 例
item_data = {"name": "my item", "description": "A great item", "price": 10.5}
item = Item(**item_data)
print(item)
#> name='My Item' description='A great item' price=10.5 tags=[]
```

### 3.4. 設定管理 (`BaseSettings`)

Pydanticは、環境変数や`.env`ファイルから設定を読み込むための`BaseSettings`クラスを提供しており、アプリケーションの設定管理に非常に便利です。

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My App"
    database_url: str
    debug_mode: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

# .envファイル
# DATABASE_URL=postgresql://user:password@host:port/db

settings = Settings()
print(settings.database_url)
```

## 4. まとめ

型アノテーションは現代的なPython開発における標準的なプラクティスです。Pydanticと組み合わせることで、堅牢で信頼性の高いアプリケーションを効率的に構築できます。
