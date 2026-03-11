"""Tests para validadores"""
import pytest

from src.utils.validators import validar_precio, validar_stock, validar_texto

def test_precio_positivo_valido():
    """Debe validar precio positivo"""
    assert validar_precio(100.0) is True
    assert validar_precio(0.0) is True

def test_precio_negativo_invalido():
    """Debe rechazar precio negativo"""
    with pytest.raises(ValueError, match="negativo"):
        validar_precio(-50.0)

def test_stock_positivo_valido():
    """Debe validar stock positivo"""
    assert validar_stock(10) is True
    assert validar_stock(0) is True

def test_stock_negativo_invalido():
    """Debe rechazar stock negativo"""
    with pytest.raises(ValueError, match="negativo"):
        validar_stock(-5)

def test_texto_valido():
    """Debe validar texto no vacío"""
    assert validar_texto("Hola") is True

def test_texto_vacio_invalido():
    """Debe rechazar texto vacío"""
    with pytest.raises(ValueError):
        validar_texto("")