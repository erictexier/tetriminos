/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 10:46:32 by etexier           #+#    #+#             */
/*   Updated: 2019/11/12 11:40:41 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int		ft_strncmp(const char *s1, const char *s2, size_t size)
{
	if (size == 0)
		return (0);
	if (*s1 == '\0' && *s2 == '\0')
		return (0);
	if (*s1 == *s2)
		return (ft_strncmp(s1 + 1, s2 + 1, size - 1));
	if ((unsigned char)*s1 > (unsigned char)*s2)
		return (1);
	return (-1);
}
