#include "libft/ft.h"
#include "mem_handler.h"
#include <unistd.h>
#include <limits.h>
#include <errno.h>

#define N 10
#define M 20

void    *ft_malloc(size_t size)
{
    if (size <= N)
    {
        ft_printf("TINY\n");
    }
    else if (size <= M)
    {
        ft_printf("SMALL\n");
    }
    else
    {
        ft_printf("LARGE\n");
    }
    
    return NULL;
}

void    ft_show_alloc_mem()
{
    ft_printf("TINY: 0xA0000\n");
    ft_printf("0xA0020 - 0xA004A : 42 bytes\n");
    ft_printf("0xA006A - 0xA00BE : 84 bytes");
    ft_printf("SMALL: 0xAD000\n");
    ft_printf("0xAD020 - 0xADEAD : 3725 bytes");
    ft_printf("LARGE: 0xB0000\n");
    ft_printf("0xB0020 - 0xBBEEF : 48847 bytes");
    ft_printf("Total: 52698 bytes\n");
}

int     main()
{
    long x = sysconf(_SC_PAGESIZE);
    ft_printf("Pagesize: %d\n", x);
    return 0;
}