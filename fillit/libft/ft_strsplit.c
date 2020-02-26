/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strsplit.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/11 14:39:45 by etexier           #+#    #+#             */
/*   Updated: 2019/11/18 17:57:51 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

static char				**free_ms_array(char **ms, char *ptr)
{
	char	**start;

	start = ms;
	while (*ms)
	{
		free(*ms);
		*ms = NULL;
		ms++;
	}
	free(ptr);
	free(start);
	return (NULL);
}

static char				**build_result(char *str,
									int len, unsigned int count, int i)
{
	char	*save_ptr;
	char	**ms;
	int		index;

	ms = (char **)malloc(sizeof(char **) * (count + 1));
	if (ms == NULL)
		return (NULL);
	index = 0;
	save_ptr = str;
	i = 0;
	while (i < len)
	{
		save_ptr = str + i;
		if (*save_ptr != '\0')
		{
			ms[index] = ft_strdup(save_ptr);
			if (ms[index] == NULL)
				return (free_ms_array(ms, str));
			i = i + ft_strlen(ms[index]);
			index++;
		}
		i++;
	}
	ms[index] = NULL;
	return (ms);
}

static char				**return_count_zero(char *ptr)
{
	char **m;

	m = (char **)malloc(sizeof(char **) * 2);
	if (m == NULL)
	{
		if (ptr != NULL)
			free(ptr);
		return (NULL);
	}
	m[0] = ptr;
	m[1] = NULL;
	return (m);
}

static unsigned int		count_field(char *str, char charset, size_t len)
{
	unsigned int		count;

	count = 0;
	while (len--)
	{
		if (*str == charset)
		{
			count++;
			*str = '\0';
		}
		str++;
	}
	return (count);
}

char					**ft_strsplit(const char *str, char charset)
{
	unsigned int		count;
	size_t				len;
	char				*ptr;
	char				**res;

	if (str == NULL)
		return (NULL);
	len = ft_strlen(str);
	ptr = ft_strdup(str);
	if (ptr == NULL)
		return (NULL);
	count = count_field(ptr, charset, len);
	if (count == 0)
		return (return_count_zero(ptr));
	res = build_result(ptr, len, count + 1, 0);
	if (ptr != NULL)
		free(ptr);
	return (res);
}
