NAME	:= test
CFLAGS	:= -Wextra -Wall -Werror
LIBFT	:= ./lib/libft

HEADERS	:= -I ./include -I ./lib/
LIBS	:= $(LIBFT)/libft.a
SRCS	:= main.c
OBJS	:= ${SRCS:.c=.o}

all: libft $(NAME)

libft:
	@$(MAKE) -C $(LIBFT)

%.o: %.c
	@$(CC) $(CFLAGS) -o $@ -c $< $(HEADERS) && printf "Compiling: $(notdir $<)"

$(NAME): $(OBJS)
	@$(CC) -g $(OBJS) $(LIBS) $(HEADERS) -o $(NAME)

clean:
	@rm -f $(OBJS)
	@$(MAKE) -C $(LIBFT) clean

fclean: clean
	@rm -f $(NAME)
	@$(MAKE) -C $(LIBFT) fclean

re: clean all

e: $(NAME)
	./$(NAME)

.PHONY: all, clean, fclean, re