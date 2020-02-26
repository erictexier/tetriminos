/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/08 18:56:08 by etexier           #+#    #+#             */
/*   Updated: 2019/11/18 16:25:17 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

static char		*st_get_start_line(const char *s)
{
	char	*ptr_start;

	ptr_start = (char *)s;
	while (*ptr_start == ' ' || *ptr_start == '\n' || *ptr_start == '\t')
		ptr_start++;
	return (ptr_start);
}

static char		*st_get_end_line(const char *s, const char *the_start)
{
	char	*ptr_end;

	ptr_end = (char *)s;
	while (*ptr_end == ' ' || \
		*ptr_end == '\n' || *ptr_end == '\t' || ptr_end == the_start)
		ptr_end--;
	return (ptr_end);
}

static char		*my_empty_char(void)
{
	char	*m;

	m = (char *)malloc(sizeof(char));
	if (m == NULL)
		return (NULL);
	*m = '\0';
	return (m);
}

char			*ft_strtrim(char const *s)
{
	char	*m;
	char	*ptr;
	char	*ptr_start;
	char	*ptr_end;
	size_t	size;

	if (s == NULL)
		return (my_empty_char());
	size = ft_strlen(s);
	ptr_start = st_get_start_line(s);
	ptr_end = st_get_end_line(s + size - 1, s);
	if (ptr_start > ptr_end)
		return (my_empty_char());
	size = ptr_end - ptr_start + 1;
	m = (char *)malloc((size + 1) * sizeof(char));
	if (m == NULL || size == 0)
	{
		return (my_empty_char());
	}
	ptr = m;
	while (ptr_start <= ptr_end)
		*ptr++ = *ptr_start++;
	*ptr = '\0';
	return (m);
}
