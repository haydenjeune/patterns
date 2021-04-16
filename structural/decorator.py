"""
Lets you attach new behaviors to objects by placing these objects inside
special wrapper objects that contain the behaviors.
"""

from abc import ABC, abstractmethod
from bz2 import compress, decompress
from typing import List, IO


class DataSource(ABC):
    @abstractmethod
    def read(self) -> bytes:
        raise NotImplementedError()

    @abstractmethod
    def write(self, data: bytes):
        raise NotImplementedError()


class DataSourceDecorator(DataSource):
    def __init__(self, inner: DataSource):
        self.inner = inner

    def read(self) -> bytes:
        return self.inner.read()

    def write(self, data: bytes):
        return self.inner.write(data)


class CompressionDecorator(DataSourceDecorator):
    def read(self) -> bytes:
        raw_data = super().read()
        data = decompress(raw_data)
        print(f"Read data:\n{raw_data}\n and decompressed to:\n{data}\n")
        return data

    def write(self, data: bytes):
        compressed_data = compress(data)
        print(
            f"Received data:\n{data}\nand writing compressed data:\n{compressed_data}\n"
        )
        return super().write(compress(data))


class EncryptionDecorator(DataSourceDecorator):
    @staticmethod
    def _super_secure_encrypt(data: bytes) -> bytes:
        return bytes([(byte + 42) % 256 for byte in data])

    @staticmethod
    def _super_secure_decrypt(data: bytes) -> bytes:
        return bytes([(byte - 42) % 256 for byte in data])

    def read(self) -> bytes:
        raw_data = super().read()
        data = self._super_secure_decrypt(raw_data)
        print(f"Read data\n{raw_data}\nand decrypted to\n{data}\n")
        return data

    def write(self, data: bytes):
        encrypted_data = self._super_secure_encrypt(data)
        print(f"Received data\n{data}\nand writing encrypted data\n{encrypted_data}\n")
        return super().write(encrypted_data)


class InMemoryDataSource(DataSource):
    def __init__(self):
        self.data: bytes

    def read(self) -> bytes:
        print(f"Read {self.data}")
        return self.data

    def write(self, data: bytes):
        print(f"Writing {data} ({len(data)} bytes)")
        self.data = data


if __name__ == "__main__":
    src = CompressionDecorator(EncryptionDecorator(InMemoryDataSource()))

    data = b"The dataaaaaaaaa"*20

    print("===== Writing =====\n")
    src.write(data)
    print("===== Reading =====\n")
    print(src.read())
