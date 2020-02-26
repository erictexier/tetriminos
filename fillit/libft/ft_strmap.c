/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/08 17:22:06 by etexier           #+#    #+#             */
/*   Updated: 2019/11/15 14:02:55 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

static char		*my_empty_case(void)
{
	unsigned char	*res;

	res = (unsigned char *)malloc(1);
	if (res == 0)
		return (char *)(NULL);
	*res = '\0';
	return ((char *)res);
}

char			*ft_strmap(char const *s, char (*f)(char))
{
	unsigned char	*ptr;
	unsigned char	*res;
	unsigned char	*ptr_res;
	size_t			size;

	if (s == NULL)
		return (char *)(NULL);
	size = ft_strlen(s);
	if (size == 0)
		return (my_empty_case());
	res = (unsigned char *)malloc((size + 1) * sizeof(char));
	if (res == NULL)
		return (NULL);
	ptr_res = res;
	ptr = (unsigned char *)s;
	while (*ptr)
	{
		*res = f(*ptr);
		res++;
		ptr++;
	}
	*res = '\0';
	return (char *)(ptr_res);
}
