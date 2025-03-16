#ifndef MEM_HANDLER_H
# define MEM_HANDLER_H

typedef t_mem_segment
{
    size_t start;
    size_t end;
}   s_mem_segment;

t_list  *init_memory(size_t size);
size_t  handle_allocate(t_list *memory, size_t len);
size_t  handle_free(t_list *memory, size_t position);

#endif