#include "calculadora.h"

double sumar(double a, double b) 
{
    return a + b;
}

double restar(double a, double b) 
{
    return a - b;
}

double multiplicar(double a, double b)
{
    return a * b;
}

double dividir(double a, double b) 
{
    if (b == 0) 
    {
        // Manejar división por cero
        return 0; // Por simplicidad, retornamos 0 en caso de división por cero
    }
    
    else
    {
        return a / b;
    }
}
