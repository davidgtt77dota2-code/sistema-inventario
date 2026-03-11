"""Tests para el servicio de productos"""
import pytest

from src.services.producto_service import ProductoService
from src.models.producto import Producto

def test_crear_producto(service):
    """Debe crear un producto"""
    producto_id = service.crear_producto(
        categoria="Electrónica",
        nombre="Cámara EZVIZ",
        precio=299.99,
        stock=5
    )
    
    assert producto_id > 0

def test_obtener_productos_todos(service):
    """Debe obtener todos los productos"""
    service.crear_producto("Cat1", "P1", 100, 5)
    service.crear_producto("Cat2", "P2", 200, 10)
    
    productos = service.obtener_productos()
    assert len(productos) == 2

def test_obtener_estadisticas(service):
    """Debe obtener estadísticas correctas"""
    service.crear_producto("Cat1", "P1", 100, 5)
    service.crear_producto("Cat2", "P2", 0, 10)
    service.crear_producto("Cat1", "P3", 50, 15)
    
    stats = service.obtener_estadisticas()
    
    assert stats['total_productos'] == 3
    assert stats['productos_con_precio'] == 2
    assert stats['stock_total'] == 30
    assert stats['categorias'] == 2