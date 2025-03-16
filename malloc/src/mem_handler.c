#include "mem_handler.h"

t_list  *init_memory(size_t size)
{
    // t_mem_segment *x = malloc()
    return ft_lstnew()
}

size_t  allocate(t_list **memory, size_t len)
{
    size_t  res;
    t_list  *current;
    t_list  *last;

    current = *memory;
    while (current)
    {
        t_mem_segment *segment = (t_mem_segment *) current->content;
        if (segment && segment->end - segment->start <= len)
        {
            res = segment->start;
            segment->start += len;
            // TODO: What happens if segment->end = segment->start
            return res;
        }
        current = current->next;
    }
    return NULL;
}

size_t  handle_free(t_list *memory, size_t position)
{

}