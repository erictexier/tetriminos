/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fillit.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eric <eric@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/21 13:55:46 by etexier           #+#    #+#             */
/*   Updated: 2020/02/05 20:22:08 by eric             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FILLIT_H
# define FILLIT_H

# define SHAPE '#'
# define EMPTY '.'
# define GRID_SIZE_MAX 11
# define SHAPES_MAX 19
# define ROW	0
# define COL	1

typedef unsigned short int	t_ushort;
typedef	struct				s_span
{
	int						start;
	int						span;
}							t_span;

typedef	struct				s_tetrino
{
	char					marker;
	char					*ptr;
	t_ushort				shape;
	int						box[2];
	int						max_box[2];
	int						cd[2];
	int						offset[4];
	struct s_tetrino		*next;
	t_span					spanx[4];
}							t_tetrino;

typedef struct				s_grid
{
	t_tetrino				*tetrino_input;
	int						sq_size;
	int						csize;
	int						marker;
	int						nb_tetrino;
	char					table2[GRID_SIZE_MAX * GRID_SIZE_MAX];
}							t_grid;

# define USAGE "usage: ./fillit a_file\n"
# define CANNOT_RD_FILE "error\n"
# define FILE_NOT_FORMAT "error\n"

t_tetrino					*ft_fillit_reader(int fd);
t_grid						*init_grid(t_tetrino *lst);
int							get_csize(t_grid *grid);
void						delete_list_tetrino(t_tetrino **lst);
t_tetrino					*make_s_tetrino(t_ushort t);

t_ushort					move_to_top(t_ushort tetrino);
t_ushort					make_tetrino(char *a, char *b, char *c, char *d);
int							is_valid_shape(t_ushort t);
int							is_on(t_ushort tetrino, int index);
void						bound(t_ushort i, int *x, int *y);
void						do_span(t_tetrino *t);
t_tetrino					*add_to_list(t_tetrino **first, t_tetrino *new);

int							resolve_iter2(t_grid *grid);
int							resize_iter(t_grid *grid);
int							display_result2(t_grid *grid);
void						init_offset(t_tetrino *t, t_grid *grid);

#endif
