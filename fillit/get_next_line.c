/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eric <eric@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/19 13:54:44 by etexier           #+#    #+#             */
/*   Updated: 2020/02/04 19:13:34 by eric             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <unistd.h>
#include "libft/libft.h"
#include "get_next_line.h"

static int			replace_none_printable(int fd, char **ptr, long len)
{
	if (!ft_isprint(ptr[fd][len]) &&
		ptr[fd][len] != '\t' &&
		ptr[fd][len] != '\v' &&
		ptr[fd][len] != '\r')
		ptr[fd][len] = '\\';
	return (len + 1);
}

static int			pop_a_line(char **ptr, int fd, char **line, ssize_t count)
{
	char	*tmp;
	long	len;

	len = 0;
	while (ptr[fd][len] != END_OF_LINE && ptr[fd][len] != '\0')
		len = replace_none_printable(fd, ptr, len);
	if (ptr[fd][len] == END_OF_LINE)
	{
		*line = ft_strsub(ptr[fd], 0, len);
		tmp = ft_strdup(ptr[fd] + len + 1);
		free(ptr[fd]);
		ptr[fd] = tmp;
		if (ptr[fd][0] == '\0')
			ft_strdel(&ptr[fd]);
	}
	else if (ptr[fd][len] == '\0')
	{
		if (count == BUFF_SIZE)
			return (get_next_line(fd, line));
		*line = ft_strdup(ptr[fd]);
		ft_strdel(&ptr[fd]);
	}
	return (1);
}

int					get_next_line(const int f, char **line)
{
	static char			*savefd[1024];
	char				*data;
	char				buffer[BUFF_SIZE + 1];
	ssize_t				count;

	if (f < 0 || line == NULL)
		return (-1);
	while ((count = read(f, buffer, BUFF_SIZE)) > 0)
	{
		buffer[count] = '\0';
		if (savefd[f] == NULL)
			savefd[f] = ft_strnew(1);
		data = ft_strjoin(savefd[f], buffer);
		free(savefd[f]);
		savefd[f] = data;
		if (ft_strchr(buffer, END_OF_LINE))
			break ;
	}
	if (count < 0)
		return (-1);
	if (count == 0 && (savefd[f] == NULL || savefd[f][0] == '\0'))
		return (0);
	return (pop_a_line(savefd, f, line, count));
}
