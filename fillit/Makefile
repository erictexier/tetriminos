# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: etexier <etexier@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 11:32:12 by etexier           #+#    #+#              #
#    Updated: 2020/02/07 11:46:19 by etexier          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

SRCS		= 	fillit.c \
				main.c \
				get_next_line.c \
				tetrino_bound.c \
				tetrino_utils.c \
				tetrino_utils1.c \
				tetrino_utils2.c \
				grid_utils.c \
				grid_utils2.c \
				resolve_iter.c


OBJS		= ${SRCS:.c=.o}

CC			= gcc

HEADERS		=  -I.

CFLAGS		= -Wall -Wextra -Werror -fPIC

LDFLAGS		= -lft -L./libft

NAME		=  fillit

AR			= ar rc

RM			= rm -f

${NAME}:		libft/libft.a ${OBJS}
				${CC} -o ${NAME} ${OBJS} ${LDFLAGS} ${CFLAGS} ${HEADERS}

all:			${NAME} 

clean:
				${RM} ${OBJS} libft/*.o

fclean:			clean
				${RM} ${NAME} libft/libft.a

re:				fclean all

.PHONY: all clean re

libft/libft.a:
				$(MAKE) -C libft