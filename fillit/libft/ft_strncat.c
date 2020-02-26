/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 10:48:48 by etexier           #+#    #+#             */
/*   Updated: 2019/11/14 16:06:07 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include "libft.h"

char	*ft_strncat(char *dest, const char *src, size_t nb)
{
	char	*ptr_save;
	size_t	size;

	ptr_save = dest;
	dest = dest + ft_strlen(dest);
	size = ft_strlen(src);
	if (size > nb)
		size = nb;
	dest[size] = '\0';
	ft_memcpy(dest, src, size);
	return (ptr_save);
}
